# runlog — one line grammar for run logs, and one reader every consumer parses

```toml
feature = "runlog"
title = "The line grammar the three run-log producers write, and the one reader every consumer parses them through"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-dLoggedFlight-1"]

[claims]
gate-legs = ["runlog selftest"]
kits = ["runlog"]
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/runlog/**",
]
```

An unattended run used to leave a snapshot rather than a sequence: its run-state file keeps the
latest phase with no time, and refusals, gate verdicts and pushes left nothing structured. The
dLoggedFlight build fixes that with journals written by each PRODUCER at the moment of the act — the
unattended driver, the gate runner and the pre-push hook — and this kit is the part they share: the
grammar, the reader, and where the files live.

## Constraints & why

**One act, one line, TAB-separated `key=value`, and nothing but four escapes.** The producers are
shell scripts, and hand-built JSON is the top breaker this repo's shell-hygiene record names; a
tracked `.jsonl` fixture is also an undeclared lexicon extension. A line of fields can be written
with one builtin `printf >>` and no process spawn, which is the producers' own cost rule.

**Field 1 is the grammar version, and a reader refuses a version it does not know.** A reader that
guessed at a v2 line would report it as data. The refusal is counted, never silent.

**A bad line is COUNTED, never dropped.** Appends from concurrent writers measured intact on node
`a`, 1600 of 1600, but the grammar does not rely on that: a torn line fails to parse and surfaces as
the bad-line count every `journal` run prints. A final line with no LF is torn by definition.

**The journal lives in the git COMMON dir, resolved with one git call.** `--path-format=absolute` is
load-bearing twice over: the bare form prints a relative `.git` in the primary tree, and
`--git-dir` from a linked worktree names `.git/worktrees/<name>`, which would split one clone's log
in two. The trap is recorded beside the unattended adopter, which met it first.

**The memory root is DECLARED, not spelled.** `resolve_memory_root` reads `MEMORY_ROOT` the way bash
sourcing reads it, because the kit ships and an adopter's root need not be `memory`. It also refuses
a root that leaves the repository, because a later unit writes under it.

**Cost is counted, not timed.** Parsing is one split per line; the self-test patches `re.compile`
and `subprocess.Popen` and counts zero of each over 100,000 lines, with a liveness probe proving the
counters can move. Wall time is printed report-only, and the leg's budget row is the cost verdict.

## Shared seams

- The producers — `TOOL-dLoggedFlight-2`, `TOOL-dLoggedFlight-3` and `TOOL-dLoggedFlight-4` — write
  this grammar, and each one's golden
  line sits in this kit's fixtures, so a producer spec that changes its data model changes the golden
  line in the same pass and the self-test reds on any key the grammar would refuse.
- The consumers — the extractor, the run model and the committed record, units 6, 8 and 9 — import
  `runlog_lib` rather than re-parsing.
- `.memory-tree.conf` — read, never written. The reader is a narrow copy of the sourced-conf grammar,
  not an import of another kit's parser, because kits are copied into adopters independently.

## Gaps

- **Retention.** Nothing prunes the journals; they grow at about 75 KB per run.
- **A line cut at a field boundary still parses.** Only a cut that breaks the grammar is caught.
- **A cut value carries no marker.** The reference writer cuts a value only after every indexed field
  has dropped, and no producer's data model reaches that step, so the case is named rather than
  instrumented.
- **The kit is waived from playbook parity** until the charter template or the runbook names it.
  That edit is a governance-carrier change outside this build's mandate; the waiver row reds the day
  either file does.

## Reuse affordance

seam: `runlog_lib.parse_line` + `read_journal` — reuse for any consumer of a run log; extend via a new
key, which every reader keeps without a code change, or a new `v`, which `GRAMMAR_VERSIONS` admits.

seam: `runlog_lib.render_line` — reuse for any writer that must fit a line under the cap; extend via
the indexed-field convention (`<base>.<n>` drops into `<base>_more`), never a second truncation rule.

seam: `runlog_lib.resolve_memory_root` — reuse for any shipped tool that must address the memory tree
without spelling its root.
