**Serves:** research PLAY-dOrderedCharter-71

# Brief: unit 71 — the adopter-name ban reads only what ships

## The prompt

> finish building this unit and PAUSE the build.

> merge this branch to remote as well

— owner, 2026-11-05. The partial close found one red its own units left, so a repair unit builds before the bar.

## The brief

### Goal

Write unit 71's spec, so `python tools/govkit/govkit.py selfcheck` reports no problem over this tree, with a fix for the class.

### Items

1. **The red.** `govkit selfcheck` fails twice: `tools/playbook/positional-refs.txt` names the adopters NicoCares and inCMS.
   - Unit 70 set `tools/playbook/kit.toml`'s gov-only lists to `role = "project-owned"`.
   - `tools/govkit/govkit.py` defines that role as "the target authors it — gov supplies no bytes for this source, ever".
   - The adopter-name ban in `tools/govkit/govkit.py#selfcheck` still builds its population from every survivor's `src`, every role included.
     Its comment says "an adopter receives a `project-owned` seed as surely as an engine", which the role's own definition contradicts.
2. **The fix.** The ban's population leaves out `project-owned` rows, and its comment says why and what it does not check.
   - Read how `resolve_entry` reports a survivor's role, and how unit 70's `check_source_rows` treats the same rows, so one reading serves both.
   - The ban must still red on a shipped file naming an adopter.
3. **The arm.** One `tools/govkit/selftest.py` arm, by the suite's own conventions:
   - a `project-owned` source naming an adopter passes;
   - the same file under a shipping role reds.
4. **Owed by unit 70.** Three new helpers are lexicon verb offenders, taking the pin from 1209 to 1212. Rename each to a declared verb, and list
   both files in Files touched:
   - `fold` in `tools/memory-tree/merge-rows.py`;
   - `split_known` and `warn_grown_file` in `tools/run-gates/owed_rows.py`.
5. **Not this unit:** the content of `positional-refs.txt`, which stays as it is.

In the spec:

- Follow `memory/TEMPLATE-SPEC.md`, at `memory/builds/dOrderedCharter/spec/2026-11-08-spec-PLAY-dOrderedCharter-71.md`.
- Status `DEFERRED`, rev-1, dated 2026-11-08, base `9f41230b5`, streams tooling, `order 17`, advancing PLAY-dOrderedCharter-38, Tier-2.
- Declare the new arm on a `New arm:` line, and each leg it moves in section 7.
- New text cites code as `path#symbol`, outside the acceptance bullets. An acceptance bullet spells a plain tracked path, with no `#` and no
  `HEAD:` prefix. New text names a section in words, and names a check by what it checks.
- Any retirement word in section 2 owes its Readers clause.
- Run the hygiene spec checks (`--only 12,25`) after the file is tracked, since they read `git ls-files`: stage it first.

### Acceptance

- The spec exists, its acceptance includes `govkit selfcheck` exiting 0 over the tree and `lexicon OK` at the pin of 1209.

### Gates

Memory hygiene, as your role runs it.

### Non-goals

- No code. No edit to another spec.
