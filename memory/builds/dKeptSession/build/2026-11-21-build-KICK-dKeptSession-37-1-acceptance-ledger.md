# KICK-dKeptSession-37 — acceptance ledger

**Serves:** journal KICK-dKeptSession-37

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. This pass re-builds the unit over the reconciled run branch at its
base `c4ef390a`; the earlier build, `ff0efc95`, was made over an older base and read only as a
reference. The criteria AC1 to AC4 were observed on win32 at that base. AC2 and AC3 ran through the
unit's own fixture CLI, `bash card-store.fixture.sh --plant fixture-run-cli`, over its own scratch
remote and repository under a short drive-letter temp directory, the spelling the suite hands the
plants; the suite that loops over `--list` was not run. The re-pointed plant `fixture-run` printed
`held` for every row the same way. `read_claude_version` and the fixture's helper `write_claude_stub`
were each graded OK by `python tools/lexicon/lexicon.py --suggest <name> --as sh.function`, and
`python tools/lexicon/lexicon.py` exited 0 over the change.

Owed to the close: every leg the spec's section 7 names, the manifest-check suite whole, whose `cli —`
block guards the extraction, and the `New arm:` line's RED-first observation, the `fixture-run-cli`
plant staged red by a copy of the engine recording `read_session_cli_version`'s answer.

## S3 — the clause of KICK-dKeptSession-12 this unit supersedes

KICK-dKeptSession-12 S1 says of the verdict line: "`<version>` is `read_session_cli_version`'s answer,
else `unknown`". That clause is superseded by name: `<version>` is `read_claude_version`'s answer, read
immediately before the fixture runs, so it names the binary the fixture's `claude -p` resolves from
PATH, else `unknown`; the writer never reads `read_session_cli_version`. Unit 12 is CLOSED, so neither
its spec nor its acceptance ledger is written here (F1, resolved (b)).

**Evidences:** KICK-dKeptSession-37
- AC1 — `grep -c 'claude --version </dev/null' skills/session-kickoff/manifest-check.sh` printed `1`
  (DERIVED, that probe), the line inside `read_claude_version`, and the body of `derive_cli_line`,
  read out by awk, names `read_claude_version` once (DERIVED, that probe). Probed alone over a stub
  `claude` first on PATH, the extracted pair printed every `cli —` line as before: the older NOTE, the
  match and the newer line, and the three skipped reasons `claude --version printed no version`,
  `claude --version did not answer within 1s` under a one-second bound (PINNED by the probe) and `no
  claude on PATH`, each from `read_claude_version`'s `unknown: <why>` at exit 1; with `AI_AGENT` unset
  the cell answered its AI_AGENT reason before any spawn, and the scratch card dir held no file after
  (DERIVED, that probe).
- AC2 — `fixture-run-cli` exported `AI_AGENT=claude-code_9-9-2_agent`, put a stub `claude` answering
  `9.9.1 (Claude Code)` first on PATH and ran `--card --fixture-run` over a `CARD_FIXTURE` stub
  exiting 0: the verdict file's line read `card-fixture — pass · fixture <blob8> · cli 9.9.1 · <iso>`,
  the verb exited 0, and the row held (DERIVED, that run). The stub's PATH entry is its POSIX
  spelling: a probe with the drive-letter spelling found the node's own `claude` first, `2.1.319`
  (DERIVED, that probe), since the drive letter's colon splits PATH.
- AC3 — the same plant's stub `claude` then printed nothing and exited 1: the next `--fixture-run`
  recorded `cli unknown`, and `--card --write --session t1`, `AI_AGENT` still naming 9.9.2, wrote the
  cell `cli — skipped: claude --version printed no version` whole. Both rows held and the plant exited
  0 (DERIVED, that run).
- AC4 — the S3 section above quotes unit 12 S1's clause through its "answer, else `unknown`":
  `tr -s ' \r\n' ' '` over this ledger piped into `grep -c "read_session_cli_version.*s answer,
  else"` printed `1` (DERIVED, that probe), and `git diff --name-only` from the pass base over unit
  12's spec and its acceptance ledger printed nothing (DERIVED, that probe, over the committed pass).
- `fixture-run`, re-pointed: KICK-dKeptSession-12 AC4's plant pinned `cli 9.9.2` from `AI_AGENT`, which
  the verdict no longer reads, so the plant now puts a stub `claude` answering 9.9.2 first on PATH; its
  five rows held (DERIVED, that run).
- seen-red — `manifest-check self-test` — red `45016a2c4` — green `45016a2c4` — `fixture-run-cli`: the verdict records `read_session_cli_version`'s answer
