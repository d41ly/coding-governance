**Serves:** research TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26

# Spec-fix brief — the check-12 edges, the spec-token hits and the unit 13 interface over the staged dWitnessedBar specs

Clear every finding below over the staged dWitnessedBar specs, changing nothing else, so that
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` prints no dWitnessedBar line and the main loop's
`python tools/check-spec-tokens.py` run prints no dWitnessedBar hit.

- The specs are uncommitted at rev-1 and unaudited, so edit them in place with no rev bump. Touch no deviation
  record. Do not commit, do not stage, and do not run the build-index generator.
- Your role admits the hygiene gate and the lexicon only. The hygiene gate reads tracked files, and the specs are
  staged in the working tree, so run `--only 2,12,25` in place and report its dWitnessedBar lines (zero is the
  target). You may not run `check-spec-tokens.py`; clear its hits by the rule each one states, which the notes below
  spell out.

## 1. Check 12 — two edges unit 15 owes back

Units 17 and 28 each declare **consumes-from** `TOOL-dWitnessedBar-15` for `test.seed`, and unit 15 declares no
matching **hands-off**. Add both to unit 15's §3, after its `TOOL-dWitnessedBar-16` bullet and in its bullet shape:
`hands-off TOOL-dWitnessedBar-17` (`test.seed`, seeding the pin, cutoff and adopter-step populations unit 17
registers) and `hands-off TOOL-dWitnessedBar-28` (`test.seed`, seeding the hand-added leg population once from
`leg_factory.py --legacy-rows`).

## 2. The spec-token hits

- **[path]** A command or literal inside backticks spells a repository path that is not tracked at HEAD, or a
  quoted path inside a Python one-liner. Pass the path as an argument instead of spelling it inside the quoted
  literal (`python - tools/gate-legs.json <<'EOF'` reading `sys.argv[1]`, say), cite a file the build creates by its
  basename, or keep a `<placeholder>` form out of backticks. Keep the criterion's meaning.
- **[guards]** §4's Files touched names `tools/gate-legs.json` (or the gotcha file in unit 26), which trips the
  guard of the named leg; add that leg (`run-gates canary`, `recall floor`) to the spec's §7 leg line.
- **[handoff]** A §3 bullet hands a token to a sibling whose spec never names it. Name the token, in backticks, in
  the sibling's spec where it reads it (its §3 consumes-from bullet or the scope item that uses it); do not drop the
  bullet. Unit 6 spells the leg ask `file_leg_ask` at three places: unit 8's §8 F4 respelled it `write_leg_ask`
  (the lexicon pin), so change all three in unit 6 to `write_leg_ask`.

## 3. Unit 13 agrees with units 16 and 18

Units 16 (§8 F3) and 18 (§8 F1, F2) read two things of unit 13's factory that unit 13's spec does not provide.
Disagreement on the interface axis is a defect in exactly one document (BUILD-METHOD M2), and here it is unit 13.
Make unit 13 provide both, in its scope and acceptance, and touch neither 16 nor 18 for this:
- `read_registrations` also reads `[[ledger]]` tables in `tools/govkit/registry.toml`, for the registries that
  repo-root tools read and for the step rows, which have no kit descriptor to register in;
- the line-number refusal admits a declared exception, `verbatim = [<field>]` on a registration, so a `file:line`
  positional reference can be stored as a key field without being read as a line key.

If unit 13 already provides either, change nothing for it and say so in your return.

## The spec-token hits, verbatim

- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-11.md [path] `a=json.loads(subprocess.run(['git','show',sys.argv[1]+':tools/gate-legs.json'],capture_output=True,text=True,encoding='utf-8').stdout);` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-11.md [path] `b=json.load(open('tools/gate-legs.json',encoding='utf-8'));` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-11.md [guards] `run-gates canary <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'run-gates canary', absent from the §7 leg line
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-14.md [path] `json.load(open('tools/gate-legs.json',` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-14.md [guards] `run-gates canary <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'run-gates canary', absent from the §7 leg line
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-19.md [path] `json.load(open('tools/gate-legs.json',encoding='utf-8'))` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-19.md [guards] `run-gates canary <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'run-gates canary', absent from the §7 leg line
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-23.md [path] `json.load(open('.claude/roles.json'))['roles']['gov-tester'];` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-23.md [path] `.claude/agents/gov-tester.md` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-26.md [guards] `recall floor <- memory/gotchas/subprocess-resolves-a-different-shell.md` — §4 files-touched names memory/gotchas/subprocess-resolves-a-different-shell.md, which trips the guard of leg 'recall floor', absent from the §7 leg line
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-4.md [path] `gate-verdict/<tree>.scoped` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-12.md [handoff] `TOOL-dWitnessedBar-12>TOOL-dWitnessedBar-22:leg.<owner>.<name>` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-12.md [handoff] `TOOL-dWitnessedBar-12>TOOL-dWitnessedBar-24:pack.portability` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-12.md [handoff] `TOOL-dWitnessedBar-12>TOOL-dWitnessedBar-28:pack.adopter` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-25.md [handoff] `TOOL-dWitnessedBar-25>TOOL-dWitnessedBar-29:warn.<n>` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-6.md [handoff] `TOOL-dWitnessedBar-6>TOOL-dWitnessedBar-2:read_verdict` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-8.md [handoff] `TOOL-dWitnessedBar-8>TOOL-dWitnessedBar-6:write_leg_ask` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
