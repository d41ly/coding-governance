# Run mandate — dLoggedFlight

**Serves:** journal TOOL-dLoggedFlight-1

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `d`, 2026-09-13. The bytes
travel here rather than as a reference, because the build folder is the authorization and may not
point at a file that can be edited after the run starts.

## The prompt

> Run this build per the protocol. Ensure it's efficiently designed aiming at performance and fully tested.

## What "this build" referred to

The prompt is deictic. In the same session the owner had asked how unattended runs could be made
transparent, and had been shown a design for tooling that records a run's action and decision
sequence: producer journals written at the moment of each act, a transcript extractor, and a
derived per-run record. That design, with the measurements and the cold review behind it, is
committed beside this file as the research record
`memory/builds/dLoggedFlight/build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md`, so a
reader who never saw the turn can still see what was meant.

## The single owner turn

The prompt path allows one question. It was spent on the choices the design had left to the owner,
four questions in one `AskUserQuestion`, answered as follows.

- **Scope:** the full design. That is the driver run log, the gate-verdict and push lines, the
  transcript extractor, the renderer with a committed per-run record and its schema check, the
  unattended Skill steps, a question-answering skill, the stuck-record drift signal and a `Decided:`
  commit-trailer rule. The owner's answer covers the governance-carrier edits this needs: the
  unattended Skill, protocol and verbs, and the build method.
- **Public record:** yes, structural only. A closed-schema record per run, carrying no free text, no
  absolute paths and no session ids, with owner interventions as counts rather than clock times, and
  a schema check enforcing it.
- **Local store:** split. Run logs live in the repo's git common dir, next to the gate logs they join
  with. Transcript extracts, which carry narration, live under the user profile.
- **Also allowed**, all four offered:
  - a new small test suite for the driver's log writer, because the standing rule bans running the
    unattended kit's existing self-test suites;
  - landing by `--no-ff` merge and push from this worktree's detached head, since the lander cannot
    run outside the primary tree, so the record ends at `LANDING`;
  - raising Claude Code's transcript retention in the owner's user settings, which was done before
    the build folder was written and lives outside this repository;
  - a backfill of this node's past runs through the extractor, with machine-local output only.

## What the run was told about scope

"Efficiently designed aiming at performance" is read as a build-level rule. Every producer's hot path
states a process-spawn budget and every consumer and suite states a wall-clock ceiling, each measured
on node `d`. "Fully tested" is read as two rules. Every unit's acceptance criteria are observed, never
asserted. Every new gate or refusal has its failing case seen RED before it lands. "Per the protocol" is
`memory/guides/UNATTENDED-PROTOCOL.md` together with `memory/guides/BUILD-METHOD.md`, both read whole
before the first unit.
