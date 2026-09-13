# TOOL-dLoggedFlight-1 — the runlog kit and its line grammar: one format every producer writes, one reader every consumer parses

**Status:** SPECCED · rev-1 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-prompt-TOOL-dLoggedFlight-1-0-run-mandate.md](../prompts/2026-09-13-prompt-TOOL-dLoggedFlight-1-0-run-mandate.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Three producers will append one line per act to a machine-local journal, and several consumers will
read those lines. Give them ONE grammar and ONE reader, shipped as a new stdlib-Python kit, so no
producer invents a format and no consumer re-parses one.

## 2. Scope (IN)

- **S1** A new kit at `tools/runlog/`: `kit.toml`, `README.md`, a `tools/govkit/registry.toml` entry
  and a codebase-map dossier `memory/map/features/runlog.md`. Observed by AC1.
- **S2** The journal location contract: the directory `runlog` under the git COMMON dir, holding one
  file per producer, `driver.log`, `gates.log` and `pushes.log`. It is a data location, not a kit
  path. Observed by AC2.
- **S3** The line grammar, stated once in the kit README and implemented once in
  `tools/runlog/runlog_lib.py`. Observed by AC2 and AC3.
- **S4** The reader: parse a line, read a journal with a count of unparseable lines, and pair `start`
  and `end` lines by nonce into invocations whose state is `ended`, `killed-or-running` or `orphan-end`.
  Observed by AC3 and AC4.
- **S5** A CLI entry `tools/runlog/runlog.py` with one subcommand here, `journal`, which prints the
  parsed lines of one producer file as JSON, with the bad-line count on stderr. Observed by AC5.
- **S6** The kit self-test `tools/runlog/selftest.py`, a new held leg `runlog selftest`, and its
  budget row. Observed by AC6.

## 3. Non-goals (OUT)

- Writing any line. The three producers are units 2, 3 and 4.
- Retention or rotation of the journal files. They grow at about 75 KB per run and nothing prunes
  them in this build; §4 records the size and the gap.
- A JSON or JSONL on-disk format. A tracked `.jsonl` file is an undeclared lexicon extension, and the
  producers are shell scripts that cannot hand-build JSON safely.
- Any consumer beyond `journal`: the model is unit 8 and the record is unit 9.

### Edges

- **hands-off** `TOOL-dLoggedFlight-2` — the driver writes lines in this grammar to `driver.log`.
- **hands-off** `TOOL-dLoggedFlight-3` — the gate runner writes lines in this grammar to `gates.log`.
- **hands-off** `TOOL-dLoggedFlight-4` — the pre-push hook writes lines in this grammar to `pushes.log`.
- **hands-off** `TOOL-dLoggedFlight-6` — the extractor imports this reader for the driver's session ids.
- **hands-off** `TOOL-dLoggedFlight-8` — the run model reads every journal through this reader.

## 4. Design

### Data model

One act is one line. A line is TAB-separated fields, and every field is `key=value`.

| rule | value |
|---|---|
| key | `[a-z][a-z0-9_.]*`; a dotted key such as `sess.CLAUDE_CODE_SESSION_ID` carries a declared name |
| value escaping | `\` becomes `\\`, TAB `\t`, LF `\n`, CR `\r`; nothing else is escaped |
| field 1 | `v=1`, the grammar version; a reader refuses a line whose `v` it does not know |
| always present | `v`, `t` (epoch seconds, `.` radix, up to six fraction digits), `p` (producer), `ev` (event) |
| `ev` values | `start` and `end` pair on `n`, the nonce; `once` is an unpaired act |
| line length | a producer truncates values so a line stays at or under 2048 bytes |
| unknown keys | preserved; a reader never drops a line for an extra key |

Small appends are atomic in practice here: 8 concurrent shell writers produced 1600 of 1600 intact
lines, measured 2026-09-13 on node `a` by the acquisition probe (PINNED). The grammar does not rely
on it: a torn line fails to parse, is counted, and surfaces as a bad-line count rather than vanishing.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `tools/runlog/runlog_lib.py` | module | none |
| `parse_line`, `read_journal`, `resolve_journal_root`, `build_invocations`, `check_line` | functions | `py.function`, each led by a declared verb |
| `Invocation`, `JournalLine` | types | `py.type`, no banned suffix |
| `KIT_RUNLOG_VERSION = "1.0"` with `# gov:kit runlog@1.0` | version pair | kit version markers |
| `tools/runlog/runlog.py` with `main` and `cmd_journal` | CLI | reserved verbs |
| `runlog selftest` | leg, `kit` / `selftests` | manifest |

`resolve_journal_root` runs `git rev-parse --path-format=absolute --git-common-dir` once, because the
bare form prints a relative `.git` in the primary tree. The trap is recorded at
`tools/unattended/adopt-unattended.sh:77-85`.

### Rollout

The kit lands with no producer writing yet, so `journal` over a fresh clone prints nothing and says
the file is absent, which is a named state, not an error.

### Files touched (estimate)

`tools/runlog/{kit.toml,README.md,runlog_lib.py,runlog.py,selftest.py}`, `tools/govkit/registry.toml`,
`tools/gate-legs.json`, `tools/govkit/subject-pins.tsv`, `tools/run-gates/selftest-budgets.txt`,
`memory/map/features/runlog.md` and the regenerated `memory/map/generated/*`.

### Alternatives rejected

- JSON lines from the producers: rejected by the shell-hygiene record of hand-built JSON as the top
  breaker, and by the lexicon's undeclared-extension refusal for a tracked `.jsonl` fixture.
- One file per slug: rejected, because gate runs and pushes carry no slug, and a per-slug path would
  make the slug a path component in three producers instead of zero.

## 5. Production-readiness checklist

- security — the reader treats every byte as data. The directory is machine-local and never pushed;
  the repo is public and nothing here is tracked except code and fixtures.
- perf / scale — parsing is one split per line. AC4 pins a throughput floor.
- error / empty / loading states — an absent file, an empty file, a torn line and an unknown `v` each
  have a named result, and none raises.
- observability — the bad-line count is always printed, so a writer that emits garbage is loud.
- risks — unbounded growth; bounded in practice at about 75 KB per run and named as a gap in §3.
- testing — `tools/runlog/selftest.py` with an assertion floor; every refusal is staged RED before
  landing.
- migration — none; the kit is new.
- user docs — the kit README states the grammar, the location contract and the CLI.

## 6. Acceptance criteria

`<kit>` below is `tools/runlog`. A file this unit creates is named only in that placeholder form here,
because the spec-tokens leg joins every path a live spec's criteria name against the tracked tree.

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs after this unit, it is green with the
  `runlog` entry claiming every file under the kit, and the codebase-map leg is green with the new
  dossier claiming the kit and its leg.
  Red when: the registry entry or the dossier claim is missing and either leg names the kit.
- **AC2** — When `parse_line` in `<kit>/runlog_lib.py` reads back a line whose values carry a TAB, a
  newline, a CR and a backslash, every value comes back byte-identical to what was written.
  Red when: the escaping is dropped from either direction and the arm compares a mangled value.
- **AC3** — When `read_journal` reads a fixture holding one torn line, one line with an unknown `v`
  and three good lines, it returns three lines and a bad count of two.
  Red when: a bad line is silently dropped, so the count reads zero.
- **AC4** — When `build_invocations` pairs a fixture of a start with its end, a start with no end and
  an end with no start, it returns one `ended`, one `killed-or-running` and one `orphan-end`, and
  parsing 100,000 lines takes under 1 s on node `d`.
  Red when: an unmatched start reads as ended, or the floor is missed.
  figure: the 1 s floor is PINNED; the measured time is printed by the arm.
- **AC5** — When `python <kit>/runlog.py journal --producer driver` runs in a clone with no journal,
  it exits 0 and prints `runlog: <path> absent` on stderr.
  Red when: an absent journal raises or prints an empty success.
- **AC6** — When `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` runs, the `runlog selftest` leg
  runs and passes at or above its assertion floor, inside its budget row.
  Red when: the leg is unbudgeted, unclaimed, or under its floor.
  cost: the held selftest chunk; this unit runs only the new leg directly.

## 7. Gates

`govkit selfcheck` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `kit version markers` · `every held leg is budgeted, every budget row resolves` · `install-prefix (shipped surface)` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · each refusal staged RED by removing its branch · floor set at landing

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "append one line per driver verb invocation to a machine-local log"`
returned no seam for a shared line grammar: its candidates were name-stem matches (`append_backlog`,
`leading_verb`) and the `.sh` layer is unscanned. The closest precedents read by hand are the gate
runner's key-per-line run record at `tools/run-gates/run-gates.sh:1288-1333` and the recall log's
JSONL. The run record's grammar is reused in spirit, one key per field and additive keys, but not as
code, because it is a whole-file key-per-line format and this one is one act per line. No existing
seam fits. The candidates and the tests that rejected them are in
`memory/builds/dLoggedFlight/build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md`.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
