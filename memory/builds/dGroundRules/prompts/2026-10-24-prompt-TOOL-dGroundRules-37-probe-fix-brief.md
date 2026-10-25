**Serves:** research TOOL-dGroundRules-37

# Probe brief — TOOL-dGroundRules-37 against the built branch, before its builder starts

## The prompt

> A read-only spec review of this spec against HEAD 7106e5abc found: §4 cites `tools/check-spec-tokens.py` `read_tracked` at a moved line and says `print_legs_for` joins guards against the tracked set, but `print_legs_for` uses that set only to mark ` (not tracked at HEAD)` and to refuse an all-untracked input, while trips come from `derive_tripped_legs`, which never consults it, so §10's reuse claim rests on a misreading; after TOOL-dGroundRules-35 (764a8a282) a warm load records `tools/govkit/govkit.py`, not the `.pyc`, so the premise that a correct build reports the `.pyc` no longer holds; TOOL-dGroundRules-33's S4 sweep was moved to the close by deviation-78; and AC4 is already green at HEAD, since `check_guard_trace` already prints `WRONG ... not under the policy fixtures guard` for every kept read once the row is renamed.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-37.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. §4 describes the join as built: trips from `derive_tripped_legs`, the tracked set only marking and refusing; §10's reuse claim is restated on that reading; cite both by symbol.
2. §1 and §4 restate the premise on the branch after TOOL-dGroundRules-35.
3. §1, S3 and §4 bind TOOL-dGroundRules-33's sweep to the close's deviation-78 sweep.
4. AC4 matches this unit's own line text (its `WRONG` naming that no `policy fixtures` row exists), so it reds only on this unit's check.
5. The status header's rev rises by one, with a §9 line naming the disagreements and the rulings. Keep the file under 48600 bytes measured with its records region; every §6 code span stays on one line; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token, and a fixture-relative path carries its target placeholder.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
The probe read HEAD 7106e5abc through `git show`; TOOL-dGroundRules-34 is being revised and rebuilt meanwhile and builds before this unit.

### Reuse
The probe record `memory/builds/dGroundRules/prompts/2026-10-24-prompt-TOOL-dGroundRules-36-1-spec-reviewer.md`'s run, quoted in the prompt above.
