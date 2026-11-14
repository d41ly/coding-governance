# Brief — aBriskDeclaration: the dispatch declaration without a process per unit, its checker beside the pass reader

**Serves:** research TOOL-aBriskDeclaration-1

## The prompt

> Make `bash tools/unattended/unattended.sh --dispatch <slug> --pass <unit> --writes <paths>` (the write-set declaration, `verb_dispatch` in `tools/unattended/unattended.sh`) fast, without loosening any refusal it makes. Do it as gov work: `/session-kickoff` first, a new build of its own with a spec, a gov-builder for the code, and landing on main through `bash tools/push-main.sh` on a green bar. The owner asked for this session, but separately decides whether this session merges or pushes main: follow the charter's [land] rule, which needs an explicit ask or a build README a run authorizes.

> A measured before and after for one whole `--dispatch` on the same frozen clone, with process counts. Every refusal and admission prints the same lines as before (prove it with `diff` over the verb's fixture or suite arms), and the parked row is identical.

The task came from the session that started this one, on the owner's request. It is quoted in part; the passages above are the ones this unit serves.

## The brief

### Goal
`--dispatch` on a large build stops paying a process pipeline per unit in its order gate, and stops waiting for the open-pass reader and then the spec-token checker one after the other. Every refusal, every note and the parked row read as they did.

### Items
1. `order_verb_of` in `tools/unattended/unattended.sh` reads the spec's first `**Status:**` line with the shell's `read`, one trailing CR dropped, and applies `ORDER_OK_RE` and `ORDER_LOOSE_RE` with `[[ =~ ]]`, so it starts no process. It leaves its answer in a variable as well as printing it, as `fact` leaves `_fact` and `normpath` leaves `_np`, and the order gate's two call sites in `verb_dispatch` read the variable with the function's stdout sent to `/dev/null`, so neither forks. The answers, `MALFORMED <loose>` included, are the old reader's.
2. `run_spec_token_check` is split at the seam `--preflight` already uses for its probes, `init_bounded` and `read_bounded` (TOOL-aBriskPreflight-4). A start half derives the key, decides the skip, resolves the launcher and starts the checker through `init_bounded`; it prints nothing and refuses nothing. The read half sits where `run_spec_token_check` is called today and prints every line and makes every refusal it makes today, in the same order, from what the start half recorded.
3. `verb_dispatch` calls the start half just before `read_open_passes`, after every refusal above it, so the checker runs while the open-pass reader runs. A refusal between the start and the read, the generator pairing or condition 1, waits for the started checker and discards its answer before it returns, as `read_preflight_probes` does: never a kill, and no checker outlives the verb.
4. The key is derived before the checker starts and recorded only after the verdict admits, as now. Nothing between the start and the read writes the tree, and the spec states that and says what would break it.
5. Comments that state the old order are made true: `run_spec_token_check`'s header, the block comment above its call in `verb_dispatch`, `order_verb_of`'s comment about `$( )`, and the verbs guide's `--dispatch` paragraph ("It runs last because it costs a tree-wide scan"), at the guide's source in the unattended kit.
6. The suite arms that pin these refusals and notes, in `tools/unattended/unattended.test.sh`: name every existing `--dispatch` arm the change must leave green unchanged, and add the arms the change owes: the order verb read with no process, the checker started before the open-pass reader and read after it, and a condition-1 refusal that leaves no checker running. Each new arm is one that can be seen red.
7. Re-key `tools/unattended/unarmed-branches.txt` where a moved `fail 49` changes an ordinal, as its earlier re-keys did.
8. Write one spec, `memory/builds/aBriskDeclaration/spec/2026-11-14-spec-TOOL-aBriskDeclaration-1.md`, Tier-2, status SPECCED, rev-1, node a, base `846d51d39`, streams tooling, order 1, in the shape `memory/TEMPLATE-SPEC.md` states, with `memory/builds/aSwiftRefusal/spec/2026-11-10-spec-TOOL-aSwiftRefusal-1.md` as the worked example of a change to this same verb. Work only in this worktree.
9. The design rests on `memory/builds/aBriskDeclaration/build/2026-11-14-build-TOOL-aBriskDeclaration-1-analysis.md`. Verify what it says of `verb_dispatch`, `order_verb_of`, `run_spec_token_check`, `init_bounded`, `read_bounded` and `read_preflight_probes` by reading that code before relying on it, and report anything in it or in this brief that is wrong.
10. A working prototype of both changes sits outside the repository, in the session scratchpad under `proto/`, as the diff `dispatch-proto.diff` against a merge of the live run's tip with main. The analysis record's after-figures are of it. Read it, state the design in the spec's own words, and improve on it where the code shows a better seam; it is untracked, so name it in prose only.
11. Decide and state each new function's and variable's name through the lexicon's `--suggest`, and what the change owes beyond the code: the codebase map, the symbols index, the kit version, the verbs guide, a `help/` page if one covers this verb's behaviour.
12. The spec states what the design does not check, starting from the analysis record's section 6 with each item verified.
13. A choice that is not derivable is a fork in the spec's open questions with a recommendation the builder can take.
14. Before returning, stage the spec and clear `python tools/check-spec-tokens.py --spec` over it and `python tools/playbook/positional.py check`. Run no whole-tree hygiene, no merge bar and no self-test suite, and do not commit. Return the spec path, its status line, each criterion's id with one line, every fork with its recommendation, and the checker's final line.

### Acceptance
- On a frozen clone of the live run's tip merged with main, one whole `--dispatch` for an order-7 unit prints the same stdout and stderr lines and parks the same row as before, by `diff`, and its trace names no `order_verb_of` process and shows the checker started before `read_open_passes`.
- The driver suite's `--dispatch` arms pass unchanged, and each new arm is observed red, then green.
- `check-arms` over the driver suite is green with the re-keyed rows.

### Gates
The driver suite's `--dispatch` arms, run directly. `check-arms` over the driver suite. The lexicon and codebase-map legs the change owes. The merge bar once at the close, without the self-test suites.

### Non-goals
- `pass_commit`, `read_attribution_tokens`, `check_pass_open` and `read_open_passes`: the live run's branch rewrote the first three, and any change there conflicts when it merges main.
- The spec-token checker's own cost, its joins and its key's inputs.
- `gate-fingerprint.sh`.
- `memory/builds/dDeclaredLoop/`, its run's worktree and its branch.
- Check 49's index-with-its-generator refusal, which stays exactly as it is.
- ANY SELF-TEST SUITE OR BAR INSIDE THE BUILD PASS, A SLICED SUITE INCLUDED. The pass runs only direct checks: `bash -n`, `check-arms` over the driver suite, the lexicon, the changed functions invoked over a hand-built fixture, the spec-token checker, and `gen_map.py --write`. The new arms are written and checked with `bash -n`; the main loop observes each red and then green at the close, and AC11's frozen-clone measurement is the main loop's.
- A pass commit without its acceptance ledger. The pass commit carries `memory/builds/aBriskDeclaration/build/2026-11-14-build-TOOL-aBriskDeclaration-1-1-acceptance-ledger.md`, one `**Evidences:** TOOL-aBriskDeclaration-1` block naming each criterion with the backticked token the criterion itself spells, and AC11 and the arms' red-then-green named as owed to the main loop at the close.
- An edit after the commit that sets the spec CLOSED: every edit lands first, and the spec's status flip is the last change of the pass.

### Limitations
- The spec's acceptance criteria name observations a pass makes directly: suite arms, probes over a fixture tree, a `bash -x` trace. The frozen-clone measurement is the main loop's, and the criterion says so. The acceptance section cites no path the unit has not built yet.
- Every spec line stating a figure with a unit carries the word PINNED or a commit sha on that line.
- No kill of a started checker: a refusal waits for it.

### Reuse
- `tools/unattended/unattended.sh#init_bounded`, `#read_bounded`, `#init_preflight_probes` and `#read_preflight_probes` are the overlap seam and its precedent.
- `tools/unattended/unattended.sh#fact` and `tools/unattended/lib-unattended.sh#normpath` are the house shape of a function that leaves its answer in a variable.
- `memory/builds/aSwiftRefusal/` moved the checker last; `memory/builds/aSmoothedDispatch/` scoped and keyed it; `memory/builds/aBriskPreflight/` built the start and read halves.

## Drawn from the session

> rc=0 wall=625.6 · git processes 192 · other traced processes 728 · order gate about 230 s · open-pass reader about 172 s · checker 152.2 s
— agent, the traced `--dispatch` on the frozen clone `dm` (the live tip `bc42f13ca` merged with `846d51d39`), node a, 2026-11-14 (PINNED)

> rc=0 wall=203.2 · git processes 193 · other traced processes 233 · stdout, stderr and the parked row identical by `diff`
— agent, the prototype on the frozen clone `da`, the same tree, node a, 2026-11-14 (PINNED)

## Owner confirmation

Asked: not asked. The session that started this one handed over the owner's request as the task above, which asks for exactly this build.
Answer: the task's own words, quoted under The prompt.
