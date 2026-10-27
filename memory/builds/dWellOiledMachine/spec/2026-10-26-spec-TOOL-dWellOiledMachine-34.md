# TOOL-dWellOiledMachine-34 — `gov trace <key>` and `gov why <key>` over the one index, one timeline engine bounded by `trace.rows`, and the health and stall logs folded into the journal grammar

**Status:** DEFERRED · rev-3 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 53 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0312@60d68fcb whole
**Carries:** node:policy-key.trace.rows

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-c.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-c.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 |
| [2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-59 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 |

<!-- /gen:spec-records -->

## 1. Goal

No record carries a key to its cause and no verb walks one: four past events each took six sources
and eight or nine lookups to rebuild (gap-rt-25), and the health and stall logs carry no key at all,
so a reap joins its bar only by the matching second (gap-rt-27). This unit gives gov `gov trace <key>`
and `gov why <key>` over the one index, re-points runlog's `build_run_model` through it and the core
reader so gov holds one timeline engine, bounds each timeline by `trace.rows` with every row filled,
`not-local: node <x>` or `pruned`, never empty, and folds the health and stall logs into the journal
grammar, keyed (P35).

## 2. Scope (IN)

- **S1** — The key's reader. `read_trace_rows(repo)` in the new `tools/runtime/trace.py` reads
  `trace.rows` (`tools/policy/catalogue.toml:1583-1587`: `60`, `120` or `all`, default `120`) once
  per verb, through `python <prefix>/policy/policy.py get trace.rows` (I31) as a subprocess; a refused
  read takes 120 with one `trace — NOTE · <why>` line. Observed by AC2.
- **S2** — `gov trace <key>`, `python trace.py trace <key>`, a `[[command]]` row of
  `tools/runtime/kit.toml` (`verb = "trace"`, `terminal = true`, a read naming no next step). The key
  is an act id (`act-<12 hex>`), a harness session id, a commit sha, a record id or an item instance
  key (I14). `read_trace_events(repo, key)` gathers, in one query: the records naming the key, the act
  records of kind `act` among them (TOOL-dWellOiledMachine-32 S7), through `record find` and
  `record show` (TOOL-dTotalRecall-9 S3, S5); the commits whose `Gov-Act:` or `Gov-Session:` trailer
  names the key or its act (TOOL-dWellOiledMachine-33), through `read_commits`
  (TOOL-dDeclaredLoop-23 S3); the journal lines keyed `act=` or `session=` for it, through
  `read_journal` (TOOL-dWellOiledMachine-16 S1) over every producer file; and the act's transcript
  pointer `transcript=<harness>:<session>` (TOOL-dWellOiledMachine-32 S6), resolved on this node by
  `resolve_session_tree` (`tools/runlog/extract.py:266`). The walk follows `made-by`, `runs-in` and
  `caused-by` (PLAY-dOrderedCharter-28 S1) one hop each way from the key and from the act it
  resolves to. Observed by AC1.
- **S3** — Every row filled. `render_trace_row(event)` prints
  `<utc> · <source> · <kind> · <subject> · <detail>`; a cell whose source lives on another node
  reads `not-local: node <x>`, `x` the act record's `node` where it is not this node's fleet tag; a
  cell whose journal window `runtime.journal` has pruned reads `pruned`, judged by the producer
  file's oldest retained `t` being later than the event's time; and an empty cell raises, so no row
  prints with a hole. Observed by AC1.
- **S4** — One timeline engine. `derive_timeline(events, rows)` orders events by
  `(t, source, kind)`, the key `build_run_model` sorts by (`tools/runlog/model.py:1853,1872`), keeps
  the newest `rows` under a number and every row under `all`, and prints
  `trace — <n> earlier row(s) beyond trace.rows <k>` when it cuts. It is the inline block
  `timeline_py`, canonical in `trace.py` and carried byte-identical by `tools/runlog/model.py` under a
  `timeline_py` row of `tools/lib/resolve-python.test.sh`'s `PARITY_ROWS`, since runlog is
  copy-installed and imports no sibling kit (TOOL-dWellOiledMachine-16 §4). `build_run_model`'s two
  sorts call it with `all`. Observed by AC2, AC5.
- **S5** — `gov why <key>`, `python trace.py why <key>`, a second `[[command]]` row (`verb = "why"`,
  `terminal = true`). `derive_why_chain(repo, key)` walks `caused-by` upward through `record show`, one
  hop per record, from the key to its act, the act's item instance key (`cause`), its work order, the
  unit's spec and the request the build's `caused-by` edge names, until a record names no cause, and
  prints `why — <hop> · <id> · <source>` per hop with S3's filling rule. Observed by AC1.
- **S6** — `build_run_model` re-pointed. Beyond S4, its record reads `read_units` (`:1500`),
  `read_ledger_lines` (`:1516`) and `read_review_records` (`:1541`) go through `record find` and
  `record show`, run as `gov_record.py` subprocesses; its journals already go through the core
  grammar's inline `read_journal` (`read_journals`, `:751-761`); and its trailer reads,
  `read_git_range` (`:592`), are TOOL-dDeclaredLoop-23's to re-point onto `read_commits`, cited and
  never re-specced. The run record built over a recorded run is unchanged field for field.
  Observed by AC5.
- **S7** — The stall log folded. `tools/unattended/stall-recorder.js` writes each stall through the
  journal writer's CLI, `python journal.py write stall session=<id> slug=<slug> error=<class>`
  (TOOL-dWellOiledMachine-16 S4), the class `stall` already one of `JOURNAL_CLASSES`, in place of its
  sidecar line. `journal.py` gains `read [--producer <p>] [--class <c>] [--key <k=v>]… [--since <epoch>]
  [--last <n>]`, printing the matching lines through `read_journal`, so no reader parses a line itself.
  The sidecar `<git-dir>/unattended/stall.<slug>.log` is retired as a write home.
  **Readers:** by name: `tools/unattended/stall-recorder.js` (:19, :24, :78), `tools/unattended/README.md`
  (:258) and `tools/unattended/unattended.sh` (:8787, :8829, :8912), whose `last-stall:` fact is
  re-pointed to S7's read verb filtered to the slug's last stall line, each in this unit · by value: `unattended.sh`'s liveness verdict prints the fact verbatim and decides nothing on it
  (`:8910-8911`). Observed by AC3.
- **S8** — The health log folded. The `health_log_py` and `health_log_sh` blocks
  (`tools/lib/health_log.py`, `tools/lib/health-log.sh`) render each event as one grammar-v1 line,
  `v=1 t=<epoch> p=health ev=once class=<event> source=<source> <key> detail=<detail>`, TAB-separated,
  appended to `<git-common-dir>/runlog/health.log`, the key `act=<GOV_ACT>`, else
  `session=<CLAUDE_CODE_SESSION_ID>`, else `session=none`; `PRODUCER_FILES` gains
  `"health": "health.log"` inside `journal_grammar_py`, so `runtime.journal` prunes it too. The
  blocks keep their signatures, their trim at `HEALTH_LOG_CAP_LINES` and their never-raise rule, and
  stay byte-identical in every carrier. `<git-common-dir>/health.log` is retired as a write home.
  **Readers:** by name: `skills/session-kickoff/manifest-check.sh` (`render_health_cell`, :600-625,
  re-pointed to S7's read verb over the `health` producer through the kit resolver it carries, :796), `skills/session-kickoff/manifest-check.test.sh` (:1821-1838) and
  `tools/check-wiring.test.sh` (:269, :1119, :1826, :1866, :1947, :1981, :2075, :2089), each in this
  unit, and the seven carriers of the blocks: `tools/lib/health_log.py`, `tools/lib/health-log.sh`,
  `skills/session-kickoff/manifest-check.sh`, `tools/check-wiring.sh`, `tools/process-monitor/reap.py`,
  `tools/run-gates/run-gates.sh` and `tools/unattended/lib-unattended.sh` · by value:
  `render_health_cell`, which counts events per source and event in a window, re-pointed above; and
  `tools/check-wiring.sh`'s `CW_HEALTH_LOG` writers (:726, :771, :1416, :1557), which only append.
  Observed by AC4.
- **S9** — The page `help/runtime.md` gains the two verbs, their key forms, `trace.rows`, the
  filling rule and the folded logs. Observed by AC6.

## 3. Non-goals (OUT)

- The act record, its cost and its transcript pointer: TOOL-dWellOiledMachine-32. The `Gov-*`
  trailers: TOOL-dWellOiledMachine-33. The binding ref and `not-local` at the landing:
  TOOL-dWellOiledMachine-39.
- The one index, `record find` and `record show`: TOOL-dTotalRecall-9, called and never re-specced.
- `read_git_range` onto `read_commits`: TOOL-dDeclaredLoop-23's consumer table.
- The journal grammar's move and retention: TOOL-dWellOiledMachine-16.
- The node-local grammars this clause does not name, the task ledger, the landed log and the recall
  queries: no clause of this unit moves them.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-16` — `write_journal_line` and `read_journal`, the lines `gov trace` reads by key and the writer the stall recorder calls
- **consumes-from** `TOOL-dWellOiledMachine-33` — `Gov-Act:`, the trailer `gov trace` walks from a commit to its act
- **consumes-from** `TOOL-dWellOiledMachine-32` — `act`, the act records whose `node`, `cause` and `transcript=` the trace and the why chain read
- **consumes-from** external — TOOL-dTotalRecall-9's `record find` and `record show`; TOOL-dDeclaredLoop-23's `read_commits`; PLAY-dOrderedCharter-28's edge types
- **hands-off** `TOOL-dWellOiledMachine-65` — S7's stall journal line and `journal.py read`, which that unit gives a `reset` key and points the limit hold at (finding 3)
- **hands-off** `TOOL-dWellOiledMachine-79` — `journal.py read` (finding 48), which the spec audit's minors batch repairs
- **hands-off** `TOOL-dWellOiledMachine-90` — `journal.py read --producer health`, through which the four suites read the health events (findings 25, 44, 67)

## 4. Design

### Evidence

- One timeline engine exists, runlog's `RunModel` (`tools/runlog/model.py:215`), built by
  `build_run_model` (`:1558`) for one run of one build; its callers are `runlog.py:389,418` and
  `record.py:1300`. There is no trace or why verb and no row cap.
- The health log's line is four TAB fields with no key (`tools/lib/health_log.py:10-14`); the stall
  sidecar's line is `<utc> <session> <class> <payload>` under `<git-dir>/unattended/`
  (`tools/unattended/stall-recorder.js:19-24`).
- One unattended run alone held 259 model events (v2:1396, the owner's AP-23), which `trace.rows`
  bounds.

### A trace, by example

```
$ python trace.py trace act-0123456789ab
2026-10-26T09:00:01Z · act · launch · act-0123456789ab · item build.unit@1·1#TOOL-fx-2 · node a
2026-10-26T09:04:10Z · journal · refusal · act-0123456789ab · rule fx-guard/locked-file
2026-10-26T09:09:55Z · git · commit · 3f9c2a71 · Gov-Act act-0123456789ab · Pass TOOL-fx-2
2026-10-26T09:10:02Z · transcript · session · 5f0c… · not-local: node b
2026-10-12T08:00:00Z · journal · stall · act-0123456789ab · pruned
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_trace_rows`, `read_trace_events`, `render_trace_row`, `derive_why_chain` | Python functions in `trace.py` | `read`, `render`, `derive`, OK |
| `derive_timeline` | Python function, inline block `timeline_py` | `derive`, OK |
| `trace`, `why` | `[[command]]` verbs of the runtime kit | none |
| `read` | `journal.py` verb | none |
| `health` | journal producer | none |
| `trace —`, `why —` | output lines | none |

Each function name was asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function`;
each printed OK.

### Migration

The two logs are node-local and capped, so no line is carried: the first write after the unit lands
starts the new file, and the old files are left where they are, read by nothing. The help page says
they may be deleted.

### Files touched (estimate)

- `tools/runtime/trace.py`
- `tools/runtime/journal.py`
- `tools/runtime/kit.toml`
- `tools/runlog/model.py`
- `tools/runlog/runlog_lib.py`
- `tools/lib/health_log.py`
- `tools/lib/health-log.sh`
- `tools/lib/resolve-python.test.sh`
- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `tools/check-wiring.sh`
- `tools/check-wiring.test.sh`
- `tools/process-monitor/reap.py`
- `tools/run-gates/run-gates.sh`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/stall-recorder.js`
- `tools/unattended/unattended.sh`
- `tools/unattended/README.md`
- `help/runtime.md`

### Alternatives rejected

- **A second timeline engine in the runtime kit.** The clause asks for one; runlog cannot import the
  runtime kit, so the engine is one inline block under a parity row.
- **Mapping the two logs' old lines at read time.** Their lines carry no key, so a read-side fold
  joins nothing gap-rt-27 asks for.

## 5. Production-readiness checklist

- security — the verbs read only; a journal line passes the grammar's redaction at write; a
  transcript on another node is named by node, never fetched.
- perf / scale — one query per verb, bounded by `trace.rows`; the walk is one hop each way.
- error / empty / loading states — an unknown key prints `trace — none · no record names <key>`; an
  unreadable key reads 120 with a NOTE.
- observability — the cut line names how many rows `trace.rows` hid.
- risks — a carrier of the health block drifting from the others; the parity row reds it.
- testing — the fixture cases AC1 to AC5 and the arms in §7.
- migration — §4 Migration.
- user docs — `help/runtime.md` (S9).

## 6. Acceptance criteria

The fixture `python trace.py --fixture` builds a scratch clone under `%TEMP%` with a short name and
replays four recorded events: an act's commit carrying `Gov-Act:`, a refusal journal line of that
act, an act whose record names node `b` and whose transcript lives there, and a stall line older than
`runtime.journal`'s cutoff.

- **AC1** — When the fixture runs, each of the four events is answered by one call of
  `python trace.py trace <key>` or `python trace.py why <key>`: the commit's trace names its act and
  session, the refusal's why chain reaches the act's item and unit, the other node's transcript row
  reads `not-local: node b`, the old stall row reads `pruned`, and no row carries an empty cell.
  Red when: any event needs a second query, or a row prints empty.
- **AC2** — When the planted policy file sets `trace.rows = 60` and the key names 75 events,
  `python trace.py trace <key>` prints 60 rows and `trace — 15 earlier row(s) beyond trace.rows 60`;
  under `all` it prints 75.
  Red when: the bound is ignored or the cut is silent.
- **AC3** — When `node stall-recorder.js` reads a planted `StopFailure` payload for a bound run,
  `runtime.log` gains a `class=stall` line keyed `session=`, no `stall.<slug>.log` is written, and
  `unattended.sh --liveness <slug>` prints that line's fields as `last-stall:`.
  Red when: the stall is written to its sidecar, or the liveness fact still reads the sidecar.
- **AC4** — When `add_health_event` runs under `GOV_ACT=act-0123456789ab`, the runlog folder's `health.log` gains
  one line `check_line` admits, carrying `p=health` and that `act`; with neither variable it carries
  `session=none`; and `manifest-check.sh --card --write` prints its `health —` cell from the new file.
  Red when: a health line carries no key, fails the grammar, or the card reads the old file.
- **AC5** — When `build_run_model` rebuilds a run from the runlog fixture's planted history, the
  output of `render_model_json` is byte-identical to the copy recorded before the unit, and the parity
  row `timeline_py` compares the block in `trace.py` with the one in `model.py`.
  Red when: the re-pointed engine moves a field, or the two copies drift.
- **AC6** — When `grep -n "trace.rows"` runs over the runtime kit's page `runtime.md`, the section
  names both verbs, the three values, `not-local` and `pruned`.
  Red when: any of them is missing.

## 7. Gates

`pre-push run-log line` · `runlog selftest` · `run-gates run-log line` · `policy fixtures` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `transition-audit arms` · `straggler-guard arms` · `measure-legs selftest` · `routed-commits selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene`

New arm: tools/runtime/trace.py · covers AC1 AC2 AC3 · the four replayed events and a planted stall, staged against a trace that walks no edge, renders an absent source as an empty cell and a liveness verb still reading the sidecar · none
New arm: tools/lib/resolve-python.test.sh · covers AC4 AC5 · one byte changed in `model.py`'s `timeline_py` block, and a health line written without its key · none

## 8. Open questions

- **F1 — Where does the one timeline engine live?** (a) An inline block canonical in `trace.py`,
  carried by `model.py` under a parity row; (b) `build_run_model` itself, called by `trace.py`; (c)
  the runtime kit importing runlog. (b) and (c) make the core depend on an observability kit, which
  the layer rule refuses (TOOL-dWellOiledMachine-16 §4). Rung 3. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F2 — What key does a health line raised outside any act or session carry?** (a) `session=none`,
  a declared absence; (b) no line at all; (c) a node key. (b) loses the node tick's own repairs, and
  (c) is a key the clause does not name. Rung 1, the clause's "journal lines keyed by act or session".
  RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F3 — Is the fold at the writers or at the reader?** (a) The writers write grammar-v1 lines, keyed;
  (b) the reader maps the old formats. (b) adds no key, so gap-rt-27's join stays impossible. Rung 1,
  gap-rt-27. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit round 1's
  promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-65, TOOL-dWellOiledMachine-79.
- rev-3 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-1
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-90.

## 10. Reuse audit

The seams extended are runlog's timeline in `build_run_model` (`tools/runlog/model.py:1558`, its
sorts at `:1853,1872`), the journal grammar's `read_journal` and the writer CLI
(TOOL-dWellOiledMachine-16 S1, S4), the health-log blocks (`tools/lib/health_log.py`,
`tools/lib/health-log.sh`), the parity table `PARITY_ROWS` in `tools/lib/resolve-python.test.sh`,
`resolve_session_tree` (`tools/runlog/extract.py:266`), and the index's `record find` and
`record show` (TOOL-dTotalRecall-9). The probe `python tools/codebase-map/reuse_lookup.py "walk every
record from a key to its cause and print a bounded timeline"` ranked `key`, `keys`, `records`, `walk`
(`tools/memory-tree/corpus_ids.py`) and `extract_records` by name stem; `walk` walks the corpus for
ids and joins no cause. Scout C's `build_run_model` callers and `read_git_range` line hold at this
base; scout C's I3 health-log claim is the four-field line confirmed at `health_log.py:10-14`.

Recall terms used: `python tools/memory-recall/query.py "how do gov trace and gov why walk a key to
its cause" --terms "gov trace gov why trace.rows not-local pruned timeline build_run_model journal
act session index"`
