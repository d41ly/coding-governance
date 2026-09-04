# The owner's prompt — build the eleven rows the triage confirmed

**Serves:** research TOOL-aMendedWarden-1 TOOL-aMendedWarden-2 TOOL-aMendedWarden-3 TOOL-aMendedWarden-4 TOOL-aMendedWarden-5 TOOL-aMendedWarden-6 TOOL-aMendedWarden-7 TOOL-aMendedWarden-8 TOOL-aMendedWarden-9 TOOL-aMendedWarden-10

Handed to `/unattended --prompt` on 2026-09-04, node `a`. The value carried whitespace and named no
readable file, so it is the prompt itself and is recorded here verbatim. The bytes travel rather than
the reference: the build folder is the authorization and may not point at a file the run can edit.

## Verbatim

> Build TOOL-aLexedStripper-4, TOOL-dScaffoldedMirror-22, TOOL-dFoldedVerdict-8,
> TOOL-aFlaggedScaffold-4, TOOL-aGroundedOrientation-4, TOOL-dTieredTribunal-16, TOOL-aCandidStub-1,
> TOOL-dUnstalledConvoy-37, TOOL-dScrubbedConduit-2, TOOL-aScouredKit-19, TOOL-aFlaggedScaffold-3.

## Where the eleven came from

They are the confirmed HIGH and CRITICAL set of a backlog triage run earlier in the same session over
all 239 open rows across the four shards. Four nominations were refuted by a skeptic stage and are
NOT in scope here: `TOOL-aGradedDoorway-9`, `TOOL-aFlaggedScaffold-5`, `TOOL-dScrubbedConduit-3` and
`TOOL-aCandidStub-2`. Each of the eleven carries a `file:line` and a reproduction in its backlog row.

## No owner question was asked, and this records why

The kickoff field set is Title, Goal, IN, OUT, Acceptance and Gates. ACCEPTANCE and GATES are the two
disqualifying fields and both are derivable: every row names its own reproduction, so acceptance is
that the reproduction stops reproducing with its failing case observed RED first per template §7, and
the gate is this repo's declared bar. The cut-line is derived and written into the README's
build-level rules. Adopting a beneficial discovery mid-run is already delegated by the
`discoveries-adopted` directive, so asking for it would have spent the only owner turn on an
authority the mandate already grants.

## What the orientation probes measured, before the roster was written

Both M5 probes ran at `d0a18683` on node `a`, before this folder existed.

**`reuse_lookup.py "a checker predicate that fails open when its input cannot be parsed"`** — 609
symbols, 184 inventory keys, 19 dossiers. The ranked seam is `agent-cap.topLevelArgs` under the
`agent-cap` dossier, plus `checkLiteralOpen` in the same file. No general fail-open helper exists;
the reuse is per-file and named per unit in each spec's §10.

**`query.py` over the decision corpus**, terms `agent-cap lexer unterminated template literal
fail-open guard verb_landed phase ordering conf parser divergence govkit argv hooksPath` — 33 hits.
Two mattered:

- **The seam for unit 1 already exists one function away.** `renderLexedView` returns
  `{code, unterminated}` at `tools/hooks/agent-cap.js:250-252`, and rule 2 falls back to the per-line
  view when that flag is set (`:663-672`, landed as `TOOL-aLexedStripper-5`). `renderBlankedView` at
  `:1039` never got the same treatment and `capFindings` at `:1115` consumes no flag. Unit 1 extends
  that seam rather than inventing a second mechanism.
- **An unlanded build exists on the same file and is SUPERSEDED, not reusable.**
  `branch/paired-lexer-followup-9c31a2` (`72dff924`, on `origin`) carries the `aPairedLexer` build:
  7 commits, a 223-line change to `agent-cap.js` modelling regex literals. Measured here: its
  merge-base with `main` is `14e21399` (2026-08-30) and `main` is **293 commits ahead** of it. Its
  `agent-cap.js` is 1247 lines against HEAD's 1610, and HEAD already carries the `renderLexedView`
  and `unterminated` work that branch predates. Rebasing it is not the cheap path and this build does
  not attempt it. The regex-literal model it holds is `TOOL-dMispairedQuote-4`, which stays OPEN and
  is outside this cut-line; that the work exists in reviewed form on a stale branch is recorded here
  so the next build for that row does not start from nothing.

## The cost this run accepts, stated because nobody priced it out loud

The build touches six kits: `hooks`, `unattended`, `govkit`, `workflows`, `memory-tree` and the
wiring check. Per `AGENTS.md` that makes the Definition of Done owe `GATE_FULL=1 GATE_SELFTESTS=1`,
which is the multi-hour bar and not the one `--close` runs — `GATE_BOUND` is 3600 s and `GATE_CMD` is
the ordinary guarded bar. The selftests for the touched kits are therefore run explicitly during the
build, per kit, rather than being discovered as a killed bar at close.
