**Serves:** research TOOL-dGroundRules-84

# Research brief — the close's bar pre-check reds, triaged into fix units

## The prompt

The main loop ran the merge bar (`bash tools/run-gates/run-gates.sh`) at `cae57b1d8`, with every unit of this build terminal: `gates RED — 10/72 legs failed`. Each of the ten failing legs was then run alone at the run's base `3c2b69be4`, and each exits 0 there, so every red is this build's. The failing legs:

- kickoff-manifest ratchet (check 9: the manifest body has not changed across ten or more watched commits; 20 non-merge commits since f221e11355)
- memory hygiene (check 25: `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md` S30 lists `loadDeclaredCap`, which no reader spells any more)
- shell hygiene (a location probe asked from a moved directory): `tools/check-template-size.sh:92-93`
- shell hygiene (a fork spent on builtin work)
- shell hygiene (a fixed-name temp renamed into place)
- spawn budget (forks per hot entrypoint)
- install-prefix (shipped surface)
- method carriers (every pointer declared)
- harness arms (fail branches armed or pinned)
- govkit runbook parity

Every failing leg's own output, extracted from the bar log, is in the run's scratchpad as `bar-reds-cae57b1d8.txt`; the whole log as `bar-precheck.log`.

## The brief

### Question
For each failing leg: which sites does it name, which of this build's commits (in `3c2b69be4..cae57b1d8`) introduced each site, and what fix does the leg's own remedy text ask for — a code change, a registry or waiver row, a pin re-measured, or a record? Then propose the fix units: one mechanism each, grouped so units sharing a file are one unit, every unit's write set named, and say which can build in parallel.

### Goal
A triage table (leg · site · introducing commit and unit · fix class · the exact fix) and a unit plan the main loop can turn into spec briefs with no further reading.

### Non-goals
Writing specs or code; legs that are green; the held self-tests.

### Method
Read each leg's checker to understand what it grades before naming a fix; run a leg's own command alone (they are bar legs, so run them on a scratch clone of `cae57b1d8` under %TEMP%/<short-name>, never in the worktree) where its output in the log is truncated. For the dSafePassage-26 finding, say whether the fix belongs in this build (restore or alias the name a live spec of another build cites) or in that build's spec, and what the charter's one-fact rule says about it. For the kickoff-manifest ratchet, read `memory/guides/SESSION-KICKOFF.md`'s audit block and say what re-stamp or body change the check wants.
