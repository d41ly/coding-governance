# Acceptance ledger — TOOL-dRetiredFork-14

**Serves:** journal TOOL-dRetiredFork-14

Tier-2 · node d · 2026-09-03

Three hooks shipped to two destinations each, byte-identical: 1610 + 394 + 207 = 2211 duplicated
tracked lines. One copy ships now, and the wired command names it.

## Acceptance criteria

**Evidences:** TOOL-dRetiredFork-14

- AC1 — MET — `git ls-files` returns exactly one path per hook: `tools/hooks/agent-cap.js`,
  `tools/hooks/scratch-guard.js`, `tools/memory-recall/recall-opened.js`
- AC2 — MET — gov's own settings were repathed by the engine itself and `bash tools/check-wiring.sh`
  exits 0, reporting `agent-cap ... at tools/hooks/agent-cap.js`
- AC3 — MET on the single-copy half, PARTIAL on the zero half. `bash tools/hooks/agent-cap.test.sh`
  passes against one copy, and both parity arms now grade the population they find rather than
  assuming two. The zero case was staged by hiding the kit copy:
  the suite refuses, rc=1. But it refuses because every OTHER arm loses its subject too, so the
  parity arm's own zero branch is verified by reading and not by execution. Recording that
  distinction rather than claiming the stronger one
- AC4 — MET — with a legacy `.claude/hooks/agent-cap.js` restored, `check-wiring.sh` prints a `note`
  naming both copies and still exits 0. `note` does not gate, which the script's own severity
  vocabulary fixes
- AC5 — MET — `bash tools/hooks/agent-cap.test.sh` passes against the surviving copy, 169 assertions
- AC6 — MET — `bash tools/check-kit-versions.sh` exits 0 after three bumps: agent-cap 1.11 to 1.12,
  settings-merge 1.1 to 1.2, memory-recall 1.5 to 1.6, every paired marker moved with its constant
- AC7 — MET, and it was the unit's real work — `merge()` now repaths: a settings file wired at
  `.claude/hooks/agent-cap.js` now has that command REPATHED in place, with no duplicate appended.
  Verified against the pre-change engine first: it returned the object unchanged, exactly as the
  criterion predicted

## What the spec treated as one class and is three

`recall-opened.js` is **claimed by no descriptor**. `agent-cap.js` and `scratch-guard.js` genuinely
resolve to two destinations; `recall-opened.js` resolves to ONE, under a `forked` rule, and the
`.claude/hooks/` copy gov tracked and wired was produced by nothing. Dropping a destination could
not have removed it — there was no destination to drop.

## The property `.claude/hooks/` had that nobody had written down

It is the same path in every repository. A `hook_path` naming it was correct for every adopter with
nothing to resolve, and that is most of why it was chosen. Naming the kit directory gives that up:
a constant naming gov's prefix is wrong in every tree installed elsewhere.

The fragments therefore declare `{kit}/hooks/agent-cap.js`, and both consumers expand it **against
the fragment's own location** — two directories up from the `.fragment.json` — rather than against
their own. That distinction is not decorative. `check-wiring.sh` is run by its self-test against
foreign fixture trees, so resolving against the checker's own prefix named files those trees do not
have; `settings-merge.py` sits in a different kit from the fragment it is handed, so resolving
against its own directory wrote commands naming the wrong kit root. Both bugs were live and both
were found by running the suites, not by reading.

The prefix gate excludes `{`-led paths in its own words, "so that a placeholder-prefixed path — the
very fix this gate exists to encourage — is not itself a hit". Using the token was therefore also
the only route that did not require growing a shrink-only waiver registry.

## What check-wiring was about to do

With the duplicate removed, its agent-cap arm printed `skip — not adopted (.claude/hooks/agent-cap.js
absent)`. The arm keyed adoption on the withdrawn file, so the repo's most important guard would have
reported a skip that reads as a pass. Its own comment explained the choice — the hook path "is not
declared anywhere this script can read" — and that reason expired the moment `hook_path` moved into
the fragment.

The arm now probes for the hook, asserts the wired command NAMES the shipped copy, and reds when it
does not. Staged and observed: pointing the command at the withdrawn path exits 1.

I also wrote that failure into the wrong accumulator on the first pass — `st=1` where this script
counts `unwired` — which would have printed UNWIRED and gated nothing. The file's own header says
only `UNWIRED` gates; the variable it gates on is two lines away in the arm beside it.

## Not done, and why

- The `.claude/hooks/` copies are removed from **gov**. Nothing is deleted from any adopter: F2 is
  ratified as leaving the withdrawal to `govkit update --write-withdrawals` on their own timing,
  because the wrong order unwires a security guard.
- The install-prefix waiver registry is keyed by `file:line` and my edits shifted it three separate
  times. Re-keyed by CONTENT each time, count unchanged at four. A line-keyed registry over a file
  anyone edits is a maintenance cost this build paid three times in one unit.
