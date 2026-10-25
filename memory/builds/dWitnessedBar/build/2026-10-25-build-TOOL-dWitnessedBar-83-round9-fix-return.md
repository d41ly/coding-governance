**Serves:** research TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84

# Round-9 fix pass — the spec writer's return

The returns of the agent dispatched from `memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-83-1-spec-writer.md`, run direct/ab1f3ca3744553c17, one per stop, extracted from its transcript by script.

## Return 1

All three spec-token hits are fixed in units 83 and 84. Since my role can't run the spec-token checker, the main loop still has to run `python tools/check-spec-tokens.py` to confirm no dWitnessedBar hit is left. Both specs were edited in place at rev-1. I touched no other spec, no `order` verb and no deviation record, and I did not stage, commit or regenerate any index.

**TOOL-dWitnessedBar-83** (`[path]`, AC1)
- The quoted grep pattern ended the path with a `'`, so the checker read `run-gates.gov.test.sh'` as an untracked file.
- AC1's command now passes the path as a separate argument and greps for it:
  `` `set -- tools/run-gates/run-gates.gov.test.sh ; for f in …; do grep -q "^New arm: $1" "$f" && …` ``
- The checker skips words that start with `$` or `"` (`tools/check-spec-tokens.py:290`), so the path is now a word of its own, and `git ls-files` lists it.
- The checker's runner pattern (`:357-361`) still finds no runner command in that token.
- The command's output is the same as before: a 24-line list ending in `44 …TOOL-dWitnessedBar-84.md`.

**TOOL-dWitnessedBar-84**
- **`[path]`, AC9:** same fix. The command is now `` `set -- memory/guides/MERGE-BAR.md ; grep -n "run-gates gov canary <- $1" memory/builds/dFairHearing/BACKLOG.md …` ``. The path is tracked, and the grep matches the same thing it matched before.
- **`[guards]`, §7:** I added `run-gates canary` to the start of the leg line. Its guard includes `{prefix}/gate-legs.json` (`tools/gate-legs.json:1141-1150`).
- **One change beyond the brief:** the sentence after the leg line used to say only `run-gates gov canary` and `measure-legs selftest` are owed for `tools/gate-legs.json`. I added `run-gates canary` to it so the prose matches the leg line. The brief said to change nothing else, so revert this if you want the leg line alone.

**What I checked**
- **My own probe:** it applies the path rule to every backticked word in both specs. No hit is left in either §6.
  - Three words outside §6 come up as untracked: 83's line 66 and the `CHARTER=`/`BAR_GUIDE=` words in 84's §4.
  - The checker only grades acceptance bullets (`:1514-1528`), so these aren't hits. They were there before my edit.
- **Hygiene gate:** `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` exits 0 and prints nothing for units 83 or 84.

**Something I noticed and left alone:** 84 §4 (lines 203-205) records `--legs-for tools/gate-legs.json` printing only the `run-gates gov canary` and `measure-legs selftest` lines. Going by the code, `--legs-for` lists `run-gates canary` under the broad guard `tools/`, so a grep for `<- tools/gate-legs.json` would not catch it. The guards check uses only the narrower guards, so it does catch `run-gates canary` through `tools/gate-legs.json`. I left this for the round-10 audit to judge.

Files:
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-83.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-84.md
