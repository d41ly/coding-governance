# Run mandate — aLeakedHandle

**Serves:** journal TOOL-aLeakedHandle-1

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `a`, 2026-09-10. The bytes
travel here rather than as a reference, because the build folder is the authorization and may not
point at a file that can be edited after the run starts.

## The prompt

> Trace both reds found here to their root cause AND the runner misreporting an external kill. Design
> and spec them separately, build per the protocol.

## What "both reds found here" referred to

The prompt is deictic: it names two reds the owner had just been shown, and a future reader cannot
see that turn. Resolved at mandate time, from the durable artifacts rather than from the transcript.

A `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` run on node `a`, 2026-09-10,
returned `gates RED — 2/104 legs failed`. The record is `<git-dir>/gate-last-failure.txt` and the
per-leg seconds are in `<git-dir>/gate-ledger.tsv`.

- `memory-hygiene self-test` — rc=124, 900.240 s, against its declared 900 s ceiling.
- `unattended kit gate` — rc=137, 4168.392 s, killed by the operator after deadlocking.

The third subject is not a red. It is the runner rendering that rc=137 as
`(timed out after 16040s, killed)`, where 16040 is the leg's declared ceiling and not the 4168 s the
ledger recorded.

## What the run was told about scope

"Design and spec them separately" is read as M2's one-mechanism-per-spec rule applied to the three
subjects above, giving three units. "Build per the protocol" is
`memory/guides/UNATTENDED-PROTOCOL.md` together with `memory/guides/BUILD-METHOD.md`, both read whole
before the first unit.

No clarification was asked. Acceptance and gates were derivable for all three units from the
artifacts named above, so the prompt path's single owner turn was not spent.
