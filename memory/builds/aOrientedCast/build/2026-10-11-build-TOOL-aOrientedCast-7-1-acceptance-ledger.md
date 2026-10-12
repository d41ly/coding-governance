# TOOL-aOrientedCast-7 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-7

Direct checks only: under the owner's rule for this run no gate, suite, slice or self-test ran in
this pass. What ran: a hand probe in the run's scratch directory that builds its own checkout (a
`.git` directory, a `.claude/roles.json` moved between absent, `{`, no `agent`-true role, empty
`harnesses` and armed, two harness scripts, three handoff files) and pipes 47 hand-built
`PreToolUse` payloads into `node tools/hooks/agent-cap.js`, reading exit code and stderr; the
suite's new `write_handoff` program run standalone over a scratch checkout, its twelve prompt
variants each piped into the hook; a staged throw in a scratch copy of the hook; payloads against
this repository for AC6 and AC7; the verifier fan-out leg's payload shape for five committed
workflow scripts, with and without `--only=scripts`; parse-only checks (`node --check`, `bash -n`);
and the lexicon. RED first: the same probe against the parent's hook (`git show HEAD:` into scratch)
admitted 33 of the 35 refusals, every one rule 6 makes, and refused the AC3 spawn after five on the
exhausted slot budget; the other two are the `--only=scripts` raw `parallel(` arm and the unknown
selector arm, which the base hook refuses as an unknown selector. Against the pass's hook 46 of the
47 met their verdict. The staged
throw exited 2 naming `staged throw`. The one probe payload that stayed red, a `scriptPath` relative
to a `cwd` other than the hook process's, passed rule 6 and was refused by the pre-existing script
read, which resolves against the process directory; a probe artifact, not a rule-6 verdict. The 47
new `rule6` arms of `agent-cap.test.sh` (§7's new arm, AC1 to AC5) were not run and are owed to the
main loop under `agent-cap self-test`, as are the `verifier fan-out` leg and the
`unattended-build self-test` arm this pass changed (spec rev-3, S11).

**Evidences:** TOOL-aOrientedCast-7
- AC1 — owed to the main loop — `agent-cap self-test` observes the `rule6 AC1` arms: a `gov-researcher` handoff admitted with an empty stderr and its `tool_use_id` in a slot, and the CRLF form with blank ends admitted. The hand probe saw both exit 0 and the slot ledger hold the id.
- AC2 — owed to the main loop — `agent-cap self-test` observes the `rule6 AC2` arms: `general-purpose`, `Explore`, an absent type and `gov-session` refused naming `gov-researcher`, and each malformed prompt refused by its cause. The hand probe saw all sixteen exit 2 with the named cause.
- AC3 — owed to the main loop — `agent-cap self-test` observes the `rule6 AC3` arms: five refused spawns then an admitted one, `slot-1` of that turn holding its id. The hand probe saw `agent-cap/S3__P3/slot-1` hold it.
- AC4 — owed to the main loop — `agent-cap self-test` observes the `rule6 AC4` arms: the listed harness by `scriptPath` with `roles` as an object and as a JSON string admitted, and the inline, name-only, unlisted, unparsable, roles-less, empty, unknown-role and `agent`-false-role calls refused. The hand probe saw those ten verdicts.
- AC5 — owed to the main loop — `agent-cap self-test` observes the `rule6 AC5` arms: no index admits as at base, `{` refuses both tools, `UNARMED` for each tool, and neither `--only=join` nor `--only=scripts` meets rule 6 while `--only=scripts` still denies a raw `parallel(`. The hand probe saw all ten verdicts.
- AC6 — `task-sha` — `handoff.py render --role gov-builder --build aOrientedCast --unit TOOL-aOrientedCast-7 --part task`, with a scratch card, this unit's spec and the build's brief, wrote a file whose `--part task` output, passed as `prompt` with `subagent_type` `gov-builder` from this repository, exited 0; `handoff.py check` re-derived `task-sha=6b1e1a63556d`, the marker's value and the hook's SHA-256 prefix of the file's `## Task` section. The rendered file was removed after the probe.
- AC7 — `tools/workflows/unattended-unit.js` — from this repository, a `Workflow` payload naming it with `roles` `{"builder":"gov-builder"}` exited 0, the same payload with `args` `{}` exited 2 naming `handoff.py harness-args`, and an `Agent` payload with `subagent_type` `Explore` exited 2 naming `gov-researcher`.
