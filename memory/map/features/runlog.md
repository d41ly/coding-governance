# runlog — one line grammar for run logs, and one reader every consumer parses

```toml
feature = "runlog"
title = "The line grammar the three run-log producers write, the one reader every consumer parses them through, the one redaction table free text passes through, the extractor that turns a session's transcripts into structural events, and the run model that joins every source into one account of one run"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-dLoggedFlight-1", "TOOL-dLoggedFlight-2", "TOOL-dLoggedFlight-4",
  "TOOL-dLoggedFlight-5", "TOOL-dLoggedFlight-6", "TOOL-dLoggedFlight-8"]

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
claim is a COUNT: over a generated population, the wrapped patterns' searches equal the hint-matched
pairs, and the wall time is printed report-only.

**The extractor keeps STRUCTURE and no free text, and it streams.** Transcripts hold the rest of a
run — every call, owner turn, compaction, limit and token — but only on the node that ran it, and the
owner's split puts extracts under the user profile, where on node `d` a sandbox group can read them.
So a command is classified in memory and dropped, labels survive only token-shaped, and the store
lives outside every repository, keyed by the git common dir so all worktrees of a clone share one.
The reader holds one parsed record per open file, which the self-test counts through the one parse
seam over a generated tree, with a hold-everything reader through the same counter as its liveness. A keepalive is JOINED to its `CronCreate` rather than matched by wording, because the
wording drifted and a prefix missed fires the join found. The self-test's own `main` aims every
ambient root at a decoy before any arm runs, since an arm that forgot one redirection would otherwise
read or write the owner's real store.

**The run model keys a run on the commit that STARTED it, and bounds every read to that run's era.**
The driver rotates a finished record in its successor's preflight commit, so a path's own creation
commit gives an archive its successor's start; with renames off, the commits that ADDED a run-state
path are the starts, one per run. A window ends at the END that moved the phase INTO a terminal one,
never at a mention of the slug, which later commits keep making. Its first cut took any END reading a
terminal phase, and the arm modeling a real landed record against a journal dated after it saw that
window end three days late, on a `--status` that read LANDED on both lines. Its git cost is constant
and counted, because a model per run over a corpus of runs must not grow with a run's commits.

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
  `runlog_lib` rather than re-parsing. The extractor, `TOOL-dLoggedFlight-6`, shipped first: it
  reads session ids off the driver journal's `start` lines through `read_journal`, runs driver
  command heads and printed narration through `render_redacted`, and persists no free text at all.
  The run model, `TOOL-dLoggedFlight-8`, shipped next: it joins the journals, the extracts, git and
  the run-state file into one run, and the committed record of `TOOL-dLoggedFlight-9` renders from it
  and reads its run starts rather than re-deriving them. The question-answering skill,
  `TOOL-dLoggedFlight-12`, prints narration through its `narration` verb.
- The unattended driver's parked-kind, owed and terminal-phase sets are COPIED into the model, and
  the withheld self-test holds each copy to the driver's source, with the fixture scaffold and the
  driver's writer key sets beside them.
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
- **The transcript format is not a contract.** An unknown record type is counted by name, but a
  renamed key reads as absent, and the fixtures are synthetic shapes written from key-and-count
  measurements, never copied. The classifier is not a shell: `bash -c`, `eval` and a quoted `$(…)`
  hide the call inside them. `--discover` is a heuristic and says so.
- **The run model infers, and says which answers are inferred.** The build commit, the owner's
  decision-log rows, an unmet acceptance line, a close's head and a call's attribution are heuristics
  named in its `method` field. It reads only history reachable from HEAD, and a git-only run's sparse
  sources read as idle gaps.
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

seam: `extract.extract_session` + `read_records` — reuse for any consumer of a Claude Code session's
transcripts; extend via a new member of `KINDS` or `CLASSES` with a fixture scenario producing it,
which the self-test demands in both directions, never a second transcript reader.

seam: `model.build_run_model` + `derive_run_starts` — reuse for any surface that reports on a run, and
the run starts for anything keyed on one; extend via a new member of `ANOMALY_KINDS`,
`CONFORMANCE_ITEMS` or `LEDGER_SOURCES` with the fixture that produces it, never a second joiner.
