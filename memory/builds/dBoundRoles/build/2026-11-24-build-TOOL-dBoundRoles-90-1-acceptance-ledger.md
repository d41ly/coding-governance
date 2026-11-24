**Serves:** journal TOOL-dBoundRoles-90

# TOOL-dBoundRoles-90 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit on its worktree before the pass commit, at base
`7a5a6d369`. The probe is a Python program in the run's scratch directory: it lifts the body of `run_wf` and the static
check's program out of `tools/workflows/unattended-build.test.sh` and runs each by `node` over the harnesses, with
`retries` 2 and the fixtures section 6 names. The same probe over the base blobs of both harnesses spawned every writing
stage twice and went on from the second return, which is the defect. No gate, suite or bar ran in the pass: the suite's
own rows, their RED-first observation and the legs of section 7 are owed to the main loop at the close.

**Evidences:** TOOL-dBoundRoles-90
- AC1 — `agent:record` — the trace held one such line and one `wrote:review` line and ended on `THROW` naming `the round was not recorded`; over the base render it held two and no throw. OWED at the close: the arm, RED on the record call put back in the helper.
- AC2 — `tools/workflows/unattended-build.js` — over the audit-off roster the trace held one `agent:commit` line and ended on `THROW` naming `the spec commit stage returned nothing`; over the base render it held two. OWED at the close: the arm, RED on the commit call put back in the helper.
- AC3 — `agent:dispose` — one line, the note naming `the disposal stage returned nothing at all`; a good disposal answered first handed the roster out; over the base render two lines and the roster handed out. OWED at the close: the arm, RED on the disposal call put back in the helper.
- AC4 — `subjects` — the check printed nothing over both templates; with the record wrapped again it named `record` by its driver word and as undeclared, with the commit or the disposal wrapped again each by name, with the resolver unwrapped and over a source holding no call it named the missing `subjects`; the probe traced two `agent:subjects` lines. OWED at the close: the suite's rows.
- AC5 — `tools/workflows/unattended-unit.js` — one `agent:build` line and `"committed":false` in the result; over the base file two lines and the second return taken. OWED at the close: the arm, RED on the marked loop put back.
- AC6 — `dispatch.args` — it carried no `retries` while the `wargs:` line carried `"retries":2`, and the grep over `tools/workflows/unattended-unit.js` printed nothing. OWED at the close: the arm, RED on the forwarding spread restored.
- AC7 — `grep -c "gov:sequential-agents(5)$" tools/workflows/unattended-build.js` — the count is 1 (DERIVED, at the pass tree), and no line of the render differs from its template line but where that line holds a token.
- AC8 — `grep -n "retries" tools/workflows/README.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/roles/SKILL.template.md .claude/skills/build/SKILL.md help/roles.md` — no line gives the key to the unit harness; the README's entry names the spec commit, the round record, the disposal and the builder as spawned once.
- AC9 — `grep -l "TOOL-dBoundRoles-5@rev-6" memory/builds/dBoundRoles/build/*TOOL-dBoundRoles-90-deviation*` — it prints the one deviation record of this unit, and the diff of the CLOSED spec from `f3ec096a8` shows no line outside its generated records region.
- seen-red — `unattended-build self-test` — red `a6f9ddc6b` — green `a6f9ddc6b` — the three writing stages spawned through runWithRetries again, DBR90 AC1 to AC3 red
