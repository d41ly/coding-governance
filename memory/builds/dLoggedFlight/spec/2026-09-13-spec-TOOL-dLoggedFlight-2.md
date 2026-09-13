# TOOL-dLoggedFlight-2 — the unattended driver writes a start and an end line for every run verb

**Status:** SPECCED · rev-1 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

The driver is the one program every unattended run calls, often a hundred times or more. Make each call
leave a start line and an end line that carry the verb, the slug, the driver's OWN exit code, the
checks it refused on, the phase before and after, and the session that called it. That covers the
refusals, phase moves, resumes and killed calls the run-state file cannot hold. It must cost no
process spawn on the hot path.

## 2. Scope (IN)

- **S1** A START line written before the argument loop, and an END line written from an EXIT trap,
  both to `driver.log` under the journal root in the grammar of `TOOL-dLoggedFlight-1`. Observed by
  AC1 and AC2.
- **S2** The END line's `rc` is the process's exit status on every in-shell path. TERM, HUP and INT
  are trapped to exit `128+n`, so the END line reads 143, 129 or 130, not the zero a bare EXIT trap
  sees. A killed call leaves its START line alone, and that absence is the signal. Observed by AC2
  and AC3.
- **S3** `fail()` appends each check number to an array, and END carries them as `checks=` in call
  order. Observed by AC1.
- **S4** START records `phase_from` from RUN.md, and END records `phase_to` read from the file after
  the verb, never inferred from `rc`, because a refused verb can still write. Both reads are pure
  bash with no fork. Observed by AC1.
- **S5** START sets `oob=1` when RUN.md is newer than the stamp the previous END left for this slug in
  this worktree. That catches an edit made outside the driver between two calls, including a git
  operation that rewrote the file. The comparison is the `-nt` builtin, with no hash. Observed by AC4.
- **S6** Session fields come from environment variables whose NAMES `.unattended.conf` declares in a
  new key, `RUNLOG_SESSION_VARS`. Each value is recorded only if it matches
  `^[A-Za-z0-9_.:-]{1,128}$`; otherwise the field is empty and `sess_bad=1` is set. Observed by AC5.
- **S7** Not journaled: `--version`, whose contract is "touching no record", and `--plan`, a
  read-only verb the merge bar calls on every run. Everything else is journaled, `--status` and
  `--resume` included. `GOV_RUNLOG=0` in the environment turns every line off. Observed by AC6.
- **S8** Spawn cost. Once the journal directory exists, a journaled call runs exactly as many
  external processes as it did before this unit. The first call in a clone pays one `mkdir`.
  Observed by AC7.
- **S9** A failed write never changes the exit code or stdout. It prints one line on stderr and the
  verb continues. Observed by AC8.
- **S10** A new small suite, `tools/unattended/runlog-writer.test.sh`, and its held leg. The owner
  approved it on 2026-09-13 because the existing unattended suites carry a standing do-not-run rule.
  Observed by AC9.
- **S11** Carriers: a run-log paragraph in the protocol's section 2, a key row in its section 8, and
  one sentence in the verbs preamble. Each goes to its template and its installed byte copy, and the
  kit version moves from 1.19 to 1.20 across its carriers. Observed by AC10.

## 3. Non-goals (OUT)

- No verb reads the log. It is evidence, never an input (protocol section 2, facts 5-7).
- No free text in a line: no `--reason`, `--item` or refusal message. Check numbers only.
- No change to any existing refusal, and no new `fail N` branch.
- No hash of RUN.md. The `-nt` stamp replaces it, and §4 states what that cannot see.
- No agent attribution. The session variables are identical in the main loop and in sidechain agents,
  measured 2026-09-12. Attribution is the extractor's job, by command and time.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-1` — the line grammar and the journal location contract.
- **hands-off** `TOOL-dLoggedFlight-8` — the run model reads these lines for the verb and phase timeline.

## 4. Design

### Placement

- `fail()` at `tools/unattended/unattended.sh:331` gains `RUNLOG_CHECKS+=("$1")`. In a subshell the
  append is lost, which only reaches `--plan`, and `--plan` is not journaled.
- The writer functions are defined with the other functions. They are installed at the last point
  where the full argv is still in `"$@"`, just before the `--waive` pre-scan at `:4925`. That is after
  the conf source at `:294`, so a conf that set its own EXIT trap is REPLACED by ours rather than
  replacing it. The install uses `builtin trap`, so a conf function named `trap` cannot intercept it.
- The START verb is `$1` when it is a declared verb. The START slug is `$2` when it matches
  `^[A-Za-z]{2,64}$`. END uses the parsed `VERB`, `SLUG`, `PH_SLUG` and the unit field from whichever
  of `BR_UNIT`, the dispatch pass, `RS_ITEM` or `RV_SUBJECT` the verb set.

### Pure-bash resolution

| value | how, with no fork |
|---|---|
| time | `${EPOCHREALTIME/,/.}`, since the radix is locale-dependent; fallback `printf -v t '%(%s)T' -1` on bash 4.x |
| git dir | `$ROOT/.git` is a directory, or a file read with `read -r` for its `gitdir:` line |
| common dir | the git dir itself, or `<git-dir>/<commondir contents>` read with `read -r` |
| phase | a `while read` over RUN.md into a variable, never `$(fact …)`, which forks |
| duration | integer microseconds from the two `EPOCHREALTIME` values |

The stamp lives in the per-worktree git dir as `runlog-stamp-<slug>`, and END updates it with `: >`.
A `-nt` comparison is mtime-based. So `oob=1` also fires after a checkout, merge or stash rewrote
RUN.md. The flag means "changed outside the driver since its last logged call", and §5 names it as
noise to be read, not an accusation.

### Data model

START: `v t p=driver ev=start n verb slug wt kit pid phase_from oob sess.<NAME>...`. END: `v t
p=driver ev=end n verb slug unit rc checks phase_to dur_us`. The nonce `n` is `<pid>.<EPOCHREALTIME
digits>`.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `write_runlog_start`, `write_runlog_end`, `read_phase_into`, `resolve_runlog_dirs` | shell functions | `sh.function`, snake_case, verb-led |
| `RUNLOG_SESSION_VARS` | conf key, `[A-Z_]` only as check 22 requires | protocol section 8 |
| `GOV_RUNLOG` | environment switch | none |
| `unattended run-log writer` | leg, `kit` / `selftests` | manifest |

### Files touched (estimate)

`tools/unattended/{unattended.sh,.unattended.conf.example,PROTOCOL.template.md,VERBS.template.md,kit.toml,runlog-writer.test.sh}`,
`.unattended.conf`, `memory/guides/UNATTENDED-{PROTOCOL,VERBS}.md`, the 15 version carriers,
`tools/gate-legs.json`, `tools/govkit/{registry.toml,subject-pins.tsv}`,
`tools/run-gates/selftest-budgets.txt`, `memory/map/features/unattended.md` and the regenerated map.

### Alternatives rejected

- One END-only line: rejected because a killed call would leave nothing. Measured: KILL leaves no trap
  line, and TERM's trap sees `$?` of 0.
- Two `git hash-object` calls per verb for out-of-band detection: rejected by S8's budget, at about
  40 ms each on node `d`.
- Logging the refusal text: rejected because it is free text carrying paths, and the check number
  plus the transcript, where local, answer the same question.

## 5. Production-readiness checklist

- security — the slug is used in a path only after it matches the slug pattern. Session values are
  shape-checked before they are written. The conf can still `exit` before the trap is installed,
  which is recorded as a known hole in the writer's header, as charter §7 requires.
- perf / scale — zero added spawns on the hot path (AC7). About two appends of under 1 ms each per call.
- error / empty / loading states — an unwritable or absent journal gives one stderr line and an
  unchanged exit code. An absent RUN.md gives an empty `phase_from`.
- observability — the killed-call signature is a START with no END. `checks=` names every refusal.
- risks — `oob` false positives after git operations, disclosed in §4. A future driver exit that
  bypasses the trap, which the suite's arm for each exit shape guards.
- testing — the new suite stages each property RED before landing, and AC7 compares exec counts from
  an xtrace, which is deterministic where wall time on this node is not.
- migration — none. An adopter who declares no `RUNLOG_SESSION_VARS` gets lines with no session fields.
- user docs — the protocol paragraph and the kit README of `TOOL-dLoggedFlight-1`.

## 6. Acceptance criteria

`<suite>` below is `tools/unattended/runlog-writer.test.sh`, which this unit creates. Every criterion
is an arm in it unless it names another command. The suite builds its own sandbox, a bare origin and
one build folder, and never runs the existing unattended suites.

- **AC1** — When `--park`, a refused `--park` (unknown argument, check 14) and `--phase` run in the
  sandbox, `driver.log` holds a START and an END for each. The END lines carry `rc=0`, `rc=1
  checks=14` and a `phase_to` read from the file.
  Red when: `fail()` stops recording checks, or `phase_to` is taken from `rc`.
- **AC2** — When a verb exits through each shell exit shape the driver has, the END `rc` equals the
  process exit status. The shapes are `exit "$status"`, an inline `--phase` exit and an unbound-variable
  error. A sandbox conf that sets its own `trap 'exit 0' EXIT` changes neither. Observed with
  `bash <suite>`.
  Red when: the trap is installed after the argument loop, so the inline exit writes no END, or
  before the conf source, so the conf's trap replaces it.
- **AC3** — When a running verb is sent TERM, its END reads `rc=143`. When one is sent KILL, its START
  stands alone and the nonce has no END.
  Red when: the signal traps are removed and the TERM end reads `rc=0`.
- **AC4** — When RUN.md is edited by a plain write between two verbs, the second START carries `oob=1`.
  When nothing touched it, the flag is absent.
  Red when: the stamp is not refreshed at END, so every START reads `oob=1`.
- **AC5** — With `RUNLOG_SESSION_VARS` naming a variable set to a UUID and one set to a value holding
  `/`, the START carries the first and records `sess_bad=1` for the second.
  Red when: an unvalidated value reaches the line.
- **AC6** — When `--version` and `--plan <slug>` run, no line is written. When `GOV_RUNLOG=0` is set,
  no verb writes a line.
  Red when: either exclusion is dropped.
- **AC7** — When `bash -x` traces `--status dLoggedFlight` with `PS4='+ ${EPOCHREALTIME} '` on this
  worktree before and after the unit, with the journal directory already present, the external-exec
  count is identical.
  Red when: the writer adds a `date`, `git` or `mkdir` call to the hot path.
  figure: the count is DERIVED at observation time; 13 was measured on 2026-09-13.
- **AC8** — When the journal directory is a file, so the append fails, the verb's exit code and stdout
  are unchanged and stderr carries one `unattended: run log` line.
  Red when: the write failure changes `rc` or prints to stdout.
- **AC9** — When `GATE_SELFTESTS=1` runs the `unattended run-log writer` leg, it passes at or above
  `FLOOR_ASSERTIONS`, prints `PASS (<n> assertions)` and finishes inside its budget row.
  Red when: the suite is unbudgeted, uncounted or under its floor.
- **AC10** — When `bash tools/unattended/adopt-unattended.sh --check` and `bash tools/check-kit-versions.sh`
  run, both are green with the protocol and verbs copies byte-identical to their templates at 1.20,
  and check 22 of `tools/unattended/check-unattended.sh` accepts the new key.
  Red when: the section 8 row or the example line is missing.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `kit version markers` · `harness arms (fail branches armed or pinned)` · `testsuite counts (every bar self-test prints one)` · `every held leg is budgeted, every budget row resolves` · `govkit selfcheck` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene`

New arm: `tools/unattended/runlog-writer.test.sh` · each AC staged RED by removing the property it observes · floor set at landing

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "append one line per driver verb invocation to a machine-local log"`
found no seam: the `.sh` layer is unscanned, and no shell writer in `tools/` appends a per-act line
today. The measured precedents are `park()` at `tools/unattended/unattended.sh:3911-3920`, which
appends with `printf >>` but forks `date`, and the gate runner's run record, which is written once
per run. This unit reuses the `printf >>` append and replaces the `date` fork with `EPOCHREALTIME`.
No existing seam fits. Rejected candidates and their tests are in the design research record.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
