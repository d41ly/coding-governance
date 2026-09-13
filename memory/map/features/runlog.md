# runlog — one line grammar for run logs, and one reader every consumer parses

```toml
feature = "runlog"
title = "The line grammar the three run-log producers write, the one reader every consumer parses them through, and the one redaction table free text passes through"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-dLoggedFlight-1", "TOOL-dLoggedFlight-2", "TOOL-dLoggedFlight-4",
  "TOOL-dLoggedFlight-5"]

[claims]
gate-legs = ["runlog selftest", "pre-push run-log line"]
kits = ["runlog"]
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = ["nt-against-a-missing-file-is-true.md",
  "trapped-signal-waits-for-the-foreground-child.md", "fixed-sleep-does-not-place-a-signal.md"]
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/runlog/**",
  ".githooks/pre-push.runlog.test.sh",
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

**A bad line is COUNTED, never dropped.** Concurrent appends measured intact, and the spec's data
model carries that measurement with its node and date, but the grammar does not rely on it: a torn
line fails to parse and surfaces as the bad-line count every `journal` run prints. A final line with
no LF is torn by definition.

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

**Redaction is ONE table of data, applied once on read, and every row carries its own proof.** The
consumers of transcript text print narration and classify command heads, and the only other redactor
in `tools/` masks `user:pass@` alone. So `redaction.tsv` holds one row per class of a closed id list,
each with a lowercase hint prefilter, a regex whose group `v` is the value, a positive and a near-miss
negative. The positives are TEMPLATES expanded at test time, because this repository is public and
push protection blocks a literal key; the self-test scans the kit's own tracked files with the table,
so a literal credential committed anywhere in it reds. Each rule compiles alone, because one combined
alternation was measured to change which rules match once inline flags go global. The prefilter's cost
claim is a COUNT: over 50,000 strings, the wrapped patterns' searches equal the hint-matched pairs.

## Shared seams

- The producers — `TOOL-dLoggedFlight-2`, `TOOL-dLoggedFlight-3` and `TOOL-dLoggedFlight-4` — write
  this grammar. The driver's writer shipped first, and its three gotcha classes are claimed here
  rather than beside the driver, whose dossier sits at its byte cap. The gate runner's shipped second,
  and its two classes are claimed by the run-gates dossier. The pre-push hook's shipped third, and
  its suite's leg is claimed HERE: no dossier claims the hook, whose two legs sit in the map
  baseline. The hook pins the bar's run id, so a push line joins its gate line exactly, and the
  runner drops that id before any leg starts. Each producer's golden line sits
  in this kit's fixtures, so a producer spec that changes its data model changes the golden line in
  the same pass and the self-test reds on any key the grammar would refuse.
- The consumers — the extractor, the run model and the committed record, units 6, 8 and 9 — import
  `runlog_lib` rather than re-parsing. The extractor, `TOOL-dLoggedFlight-6`, is specced to run
  command heads and printed narration through `render_redacted` and to persist no free text at all.
- The gate runner's own `redact()` stays separate: it masks leg output on write, under its own stated
  scope, and this table does not replace it.
- `.memory-tree.conf` — read, never written. The reader is a narrow copy of the sourced-conf grammar,
  not an import of another kit's parser, because kits are copied into adopters independently.

## Gaps

- **Retention.** Nothing prunes the journals; the spec's non-goals carry the growth estimate.
- **A line cut at a field boundary still parses.** Only a cut that breaks the grammar is caught.
- **A cut value carries no marker.** The reference writer cuts a value only after every indexed field
  has dropped. The driver reaches that step, since its slug, worktree path and phase are unbounded and
  it writes no indexed family, so `TOOL-dLoggedFlight-2` fits its lines by that rule and its suite
  compares them with `render_line`. The gate runner reaches both steps, dropping `fail.<i>` fields
  first and then cutting its run id, and `TOOL-dLoggedFlight-3`'s suite compares each the same way.
  So does the pre-push hook, dropping `ref.<i>` fields and then cutting the longest value, graded the
  same way by `TOOL-dLoggedFlight-4`'s suite. Nothing on a cut line says it was cut.
- **Redaction misses what it has no shape for.** A class nobody listed, a bare value printed with no
  key beside it, and a head truncated before a row's minimum length all pass through. The README lists
  them, and a new class is one id, one row and its positive.
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

seam: `runlog_lib.render_redacted` + `scan_secrets` — reuse for any free text a tool prints or
classifies; extend via one row in `redaction.tsv` and its id in `CLASS_IDS`, never a second redactor.
