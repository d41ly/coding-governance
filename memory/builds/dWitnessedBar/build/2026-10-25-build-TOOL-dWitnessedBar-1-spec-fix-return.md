**Serves:** research TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-28

# Spec-fix pass — the spec writer's returns

The returns of the agent dispatched from `memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-4-spec-writer.md`, run direct/abd4550f322284957, one per stop (the pass, then two follow-ups the main loop sent), extracted from its transcript by script.

## Return 1

All the brief's findings are fixed, and so is the extra unit 5 item you sent. `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`, run in place, exits 0 and prints no dWitnessedBar finding. Its only dWitnessedBar lines are five "did not grade — READER NOT IN TREE" notes on units 20 and 24, which were there before this pass. I did not run `check-spec-tokens.py`. Instead I wrote a small script that does the same handoff and acceptance-path checks over the 30 specs (56 hands-off bullets, 243 acceptance bullets), and it finds nothing. No rev bump, no deviation record, nothing staged or committed, no index run.

**1. Check 12 edges.** Unit 15's §3 now hands off to 17 and 28, after its unit 16 bullet, in the wording you gave.

**2. Spec-token hits**
- **[path]**
  - Units 11 (AC2), 14 (AC10), 19 (AC5) and 23 (AC4): each Python one-liner now takes the file as an argument (`... tools/gate-legs.json`, `... .claude/roles.json`) and reads it through `sys.argv`.
  - Unit 23's Red-when names the render by its basename, `gov-tester.md` under `.claude/agents/`.
  - Unit 4 AC3 is now `<common-dir>/gate-verdict/<tree>.scoped`, the same form as its AC1.
- **[guards]** `run-gates canary` added to the §7 leg line of units 11, 14 and 19; `recall floor` added to unit 26's.
- **[handoff]**
  - Units 22, 24 and 28 now name `leg.<owner>.<name>`, `pack.portability` and `pack.adopter` in their consumes-from bullets from unit 12.
  - Unit 2 names `read_verdict` in its consumes-from bullet from unit 6, tied to unit 6's S10.
  - Unit 6 says `write_leg_ask` in all three places.
  - Unit 25 → 29 was fixed the other way: I changed unit 25's `warn.<n>` to unit 29's spelling, `warn.<k>`, in both places. Naming `warn.<n>` in unit 29 would have left two spellings of one key.

**3. Unit 13.** It provided neither thing, so I added both:
- S2 and §4 now say `read_registrations` also reads `[[ledger]]` tables in `tools/govkit/registry.toml`. govkit's own `load_registry` (`govkit.py:247`) reads only its own tables, so the new tables don't affect it. Copy-installed adopters have no govkit registry and register through their kit descriptors only.
- A new S11 adds the optional `verbatim = [<field>]` key. It exempts only the named fields of that one registration from the line-number refusal. `read_rows` takes a `verbatim` argument, and a `verbatim` entry not listed in `fields` is refused.
- New AC9 and AC10 cover these, the `resolve-python.test.sh` arm now covers them too, and the hand-offs to units 16 and 18 name `read_registrations` and `verbatim`. Units 16 and 18 are untouched.

**4. Unit 5, gap-test-09.** New S8:
- **Guards.** Every held leg selected by the `kit` rule (subject `kit` or chunk `selftests`) must carry a non-empty `guard` or a descriptor-only `unguarded_why` reason, never both. A new `held guard` arm in `leg_factory.py --conform` enforces this, and the count line gains `<h> held · <u> unguarded`.
- **The eight legs.** There are eight unguarded held legs, out of 71 held legs among 142 rows at `19d6aae6`; S8 lists them. Two already state their reason in comments, and that text moves into the key.
- **README.** The typed `43/43 … (42 held …)` figure at `tools/run-gates/README.md:98` becomes a template with placeholders, and the README points at the `--conform` count line for the real number.
- **Acceptance.** New AC7 is seen red on a planted held leg with no guard and no reason, and again with an empty reason. A `New arm:` line is added.
- **Files and legs.** Files touched gains the leg factory, `tools/gate-legs.json` and the six declaration files. The §7 leg line gains the legs those files trip: `run-gates gov canary`, three `govkit` legs, `recall floor arms` and four workflows-kit legs.
- **Scope limit.** Legs held by `quarantine` or `level` are out of scope for the arm, because they are picked per run, not by the manifest row.
- **Edge.** The new consumes-from bullet on unit 11 failed check 12, so I added the matching hands-off to unit 5 in unit 11's §3.

**Left for you:**
- Unit 4 line 70 still says `warn.<n>`. No check flags it, so I left it, but it should become `warn.<k>`.
- Unit 24's §3 and §8 F7 still say gap-test-09's two remaining parts go to a BACKLOG ask. Unit 5 now carries them, so that ask isn't needed and F7's wording is out of date.
- `memory/builds/dWitnessedBar/BACKLOG.md` has changes in the working tree that I did not make; I left it alone.

Files changed, all under `C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\`:
- 2026-10-25-spec-TOOL-dWitnessedBar-2.md
- 2026-10-25-spec-TOOL-dWitnessedBar-4.md
- 2026-10-25-spec-TOOL-dWitnessedBar-5.md
- 2026-10-25-spec-TOOL-dWitnessedBar-6.md
- 2026-10-25-spec-TOOL-dWitnessedBar-11.md
- 2026-10-25-spec-TOOL-dWitnessedBar-13.md
- 2026-10-25-spec-TOOL-dWitnessedBar-14.md
- 2026-10-25-spec-TOOL-dWitnessedBar-15.md
- 2026-10-25-spec-TOOL-dWitnessedBar-19.md
- 2026-10-25-spec-TOOL-dWitnessedBar-22.md
- 2026-10-25-spec-TOOL-dWitnessedBar-23.md
- 2026-10-25-spec-TOOL-dWitnessedBar-24.md
- 2026-10-25-spec-TOOL-dWitnessedBar-25.md
- 2026-10-25-spec-TOOL-dWitnessedBar-26.md
- 2026-10-25-spec-TOOL-dWitnessedBar-28.md

## Return 2

Both leftovers are fixed, in place with no rev bump and nothing staged. The hygiene check still exits 0 with no dWitnessedBar findings.

1. **Unit 4, line 70:** `warn.<n>` is now `warn.<k>`. No spec in the folder still says `warn.<n>`.
2. **Unit 24:**
   - **§3:** the gap-test-09 non-goal now says the stale README figure and the eight unguarded held legs are carried by TOOL-dWitnessedBar-5 S8.
   - **§8 F7:** it now lists three options: this unit, a BACKLOG ask, or unit 5. It is marked RESOLVED (main loop, 2026-10-25) with the third option, citing unit 5 S8. Unit 24 keeps the PowerShell part through its own S12.
   - **Edges:** I added no §3 edge in either direction. Unit 24 and unit 5 each close part of gap-test-09 but pass nothing to each other, so check 12 has nothing to match. F7 says this.

`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`, re-run in place, exits 0 and ends with `HYGIENE --only 2,12,25 ran checks 2 12 25`. It prints five dWitnessedBar lines, the same five as before this pass. All are check-25 "did not grade — READER NOT IN TREE" notes, not failures:
- unit 20 S2: `policy.py lists`, `legacy-homes`, `check_policy.py`
- unit 24 S14: `tools/playbook/core.py meta-check`, `core-pending.txt`

Files changed in this round:
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-4.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-24.md

## Return 3

Done: line 359 of unit 24 (C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-24.md) now reads `RESOLVED (agent, 2026-10-25, delegated): (c), …` with the rest unchanged; I didn't re-run the hygiene check.
