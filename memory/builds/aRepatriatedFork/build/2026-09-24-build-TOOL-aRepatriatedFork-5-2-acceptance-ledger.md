# TOOL-aRepatriatedFork-5 — acceptance ledger, closing review round 1 fold A

**Serves:** journal TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-8

The FOLD pass for closing review round 1 items B1, H1 and M1, under the mandate. It ran no merge bar
and no self-test suite. Each new arm was run as a SLICE, meaning the suite's prologue plus only the
new blocks in a temp script, or by importing `.githooks/pre_push_bar_selftest.py` and calling the
one arm function. Every slice ran first against the c6513db0 bytes and was observed RED, then ran
against this fold and was observed green.

## The fixtures

- **Bar fixture**: `pre_push_bar_selftest.Fixture` under `%TEMP%/rf5`, with the default bar stubbed
  RED, a declared GREEN `scripts/unattended-bar.sh`, an undeclared GREEN `scripts/other-bar.sh`,
  `.unattended.conf` declaring the first as `GATE_CMD`, and `gatepayload` and `x.pyc` on PATH.
- **Lander slice**: `tools/push-main.test.sh` prologue plus cases 9, 9b, H1 and H1b, in a clone of
  c6513db0 under `%TEMP%/rf5c`, first with that clone's own hook and lander, then with this fold's.
- **Hook slice**: `.githooks/pre-push.test.sh` prologue, its decision helpers, arms 25-29b and the
  `incms` section, in the same clone and the same two states.

**Evidences:** TOOL-aRepatriatedFork-5
- AC11 — `bash gatepayload scripts/unattended-bar.sh` — c6513db0's hook landed it and `sh x.pyc scripts/unattended-bar.sh`, each rows 9 and 10 reporting the push LANDED; this fold refused both with `would RUN 'gatepayload'` and `would RUN 'x.pyc'` and no `PAYLOAD RAN`
- AC12 — `bash scripts/other-bar.sh` — c6513db0's hook landed it as row 11; this fold refused it with `neither this kit's own runner`, landed the declared value with END `bar_path=scripts/unattended-bar.sh`, and push-main's marker read `<sha> by push-main bar tracked bar.sh <blob>`, where c6513db0's marker carried no bar
- AC10 — amended rev-3 — the mutation now also disables the executed-word and declared arms, and under it `bash gatepayload scripts/unattended-bar.sh` and `bash scripts/other-bar.sh` landed with their own text printed; logged in section 9's rev-3 line

**Evidences:** TOOL-aRepatriatedFork-8
- AC12 — `tools/push-main.sh` — with `GOV_GATE_CMD_TEST=1` and `GOV_GATE_CMD=true` set only in `.githooks/gate-env.sh`, c6513db0's lander wrote the marker for a committed copy and for a copy hidden by `.git/info/exclude`, and c6513db0's hook sourced an untracked copy on a feature push; this fold landed the committed copy with no marker and `STUB` named, refused the excluded copy so nothing landed, and refused the untracked feature-push copy as `bar-refused`

## Not run here

The merge bar and the suites `pre-push bar self-test`, `pre-push self-test`, `pre-push run-log line`
and `push-main self-test`, whose files this fold edited, are owed at the close. A slice of the
run-log suite's DEC, AC7 and EXITS blocks showed DEC green and the exit table counting three
`bar-refused` sites. The same slice showed AC7's "writer adds no external exec" RED by one `git`
exec, and it is equally RED against c6513db0's bytes, so this fold did not cause it.
