# TOOL-dLoggedFlight-2 — the unattended driver writes a start and an end line for every run verb

**Status:** CLOSED · rev-6 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-build-TOOL-dLoggedFlight-2-1-acceptance-ledger.md](../build/2026-09-13-build-TOOL-dLoggedFlight-2-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md](../prompts/2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md) | journal | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

The driver is the one program every unattended run calls, often a hundred times or more. Make each call
leave a start line and an end line that carry the verb, the slug, the driver's OWN exit code, the
checks it refused on, the phase before and after, and the session that called it. That covers the
refusals, phase moves, resumes and killed calls the run-state file cannot hold. It must cost no
process spawn on the hot path and must not change how the driver dies.

## 2. Scope (IN)

- **S1** A START line written before the argument loop, and an END line written from an EXIT trap,
  both to `driver.log` under the journal root in the grammar of `TOOL-dLoggedFlight-1`. From a linked
  worktree the line lands in the common dir, never under `.git/worktrees/`. The END line's `unit` and
  `slug` fields follow the per-verb rule in §4. Observed by AC1, AC11 and AC13.
- **S2** END carries `rc` and `exit=clean|unclean`. Every shell exit the driver makes after the
  trap is installed sets a clean-exit marker immediately before it, so `exit=clean` means the driver
  chose its exit and `rc` is that exit's status. A call killed by a signal reaches the EXIT trap with
  no marker and records `exit=unclean`. No TERM, HUP or INT trap is installed, so a signal still ends
  the driver as promptly as it does today. A call killed by KILL leaves its START alone, and that
  absence is the signal. Observed by AC2 and AC3.
- **S3** `fail()` appends each check number to an array, and END carries them as `checks=` in call
  order. Observed by AC1.
- **S4** START records `phase_from` from RUN.md, and END records `phase_to` read from the file after
  the verb, never inferred from `rc`, because a refused verb can still write. Both reads are pure
  bash with no fork. Observed by AC1.
- **S5** START sets `oob=1` when RUN.md is newer than the stamp the previous END left for this slug in
  this worktree. That catches an edit made outside the driver between two calls, including a git
  operation that rewrote the file. The comparison is the `-nt` builtin, with no hash. With no stamp
  yet, `oob` is omitted: `-nt` against a missing file is true, and a first call is not an edit.
  Observed by AC4.
- **S6** Session fields come from environment variables whose NAMES `.unattended.conf` declares in a
  new key, `RUNLOG_SESSION_VARS`. Each value is written as `sess.<NAME>=<value>` only if it matches
  `^[A-Za-z0-9_.:-]{1,128}$`; otherwise the field is empty and `sess_bad=1` is set. An unset or empty
  variable writes no field and no flag, because absence is a state and not a refusal. A declared name
  that is not a shell identifier sets `sess_bad=1`. At most eight names are read, and any beyond them
  are counted in `sess_more`. Observed by AC5.
- **S7** Not journaled: `--version`, whose contract is "touching no record", and `--plan`, a
  read-only verb the merge bar calls on every run. Everything else is journaled, `--status` and
  `--resume` included. `GOV_RUNLOG=0` in the environment turns every line off. Observed by AC6.
- **S8** Spawn cost. Once the journal directory exists, a journaled call runs exactly as many
  external processes as it did before this unit. The first call in a clone pays one `mkdir`.
  Observed by AC7.
- **S9** A failed write never changes the exit code or stdout. It prints one line on stderr and the
  verb continues. Observed by AC8.
- **S10** A new small suite, `tools/unattended/runlog-writer.test.sh`, approved by the owner on
  2026-09-13. It is withheld from adopters in `tools/unattended/kit.toml`'s `project-owned` list and
  budgeted as a non-held row in `tools/run-gates/selftest-budgets.txt`. It is NOT a gate leg: the
  2026-08-23 owner ruling in `tools/unattended/kit.toml` keeps this kit's self-tests off the bar, and
  TOOL-aQuenchedHarness-3 keeps them out of adopters' trees. `run-unattended-gates.sh` derives its
  population from the budget rows and so picks it up with its siblings; a build bound not to run
  those siblings runs this suite alone, directly. Observed by AC9.
- **S11** Carriers: a run-log paragraph in the protocol's section 2, a key row in its section 8, and
  one sentence in the verbs preamble. Each goes to its template and its installed byte copy, and the
  kit version moves from 1.19 to 1.20 across its carriers. Observed by AC10.
- **S12** Three gotcha records under `memory/gotchas/`: `-nt` against a missing file is true; a
  trapped signal waits for the foreground child; and a fixed sleep before a signal does not place the
  signal inside the child it means to interrupt. Each is registered with `gotchas.py --write` and
  claimed by a dossier. Observed by AC12.

## 3. Non-goals (OUT)

- No verb reads the log. It is evidence, never an input (protocol section 2, facts 5-7).
- No free text in a line: no `--reason`, `--item` or refusal message. Check numbers only.
- No change to any existing refusal, exit code or signal behaviour, and no new `fail N` branch.
- No hash of RUN.md. The `-nt` stamp replaces it, and §4 states what that cannot see.
- No agent attribution. The session variables are identical in the main loop and in sidechain agents,
  measured 2026-09-12. Attribution is the extractor's job, by command and time.
- No gate leg for the suite (S10).

### Edges

- **consumes-from** `TOOL-dLoggedFlight-1` — the line grammar and the journal location contract.
- **hands-off** `TOOL-dLoggedFlight-8` — the run model reads these lines for the verb and phase timeline.
- **hands-off** `TOOL-dLoggedFlight-11` — the protocol paragraph this unit adds, which unit 11 extends.

## 4. Design

### Placement

- `fail()` at `tools/unattended/unattended.sh:331` gains `RUNLOG_CHECKS+=("$1")`. In a subshell the
  append is lost, which only reaches `--plan`, and `--plan` is not journaled.
- The writer functions are defined with the other functions. They are installed at the last point
  where the full argv is still in `"$@"`, just before the `--waive` pre-scan at `:4925`. That is after
  the conf source at `:294`, so a conf that set its own EXIT trap is REPLACED by ours rather than
  replacing it. The install uses `builtin trap`, so a conf function named `trap` cannot intercept it.
- Every shell exit after the install sets `RUNLOG_CLEAN=1` first. The sites are `:4973`, `:5009`,
  `:5015`, `:5019`, `:5020`, `:5021`, `:5032`, `:5039`, `:5040` and `:5059`. A marker on an exit that
  is not journaled, as `--plan`'s and `--version`'s are not, is harmless. The suite enumerates every `exit` across the whole of `tools/unattended/unattended.sh`
  and `tools/unattended/lib-unattended.sh`, excluding awk program text and comments, and fails on one
  without the marker. The only exemptions are the named pre-install lines `:74`, `:275`, `:276`, `:279`
  and `:310`. So an exit added later inside a verb body, the likeliest place, cannot slip past. The
  suite names each exemption by its line's TEXT, never its number, and requires each text to match
  exactly one site above the install: this unit's own insertions move the numbers, and a second copy
  of an exempt line is an exit nobody exempted.
- The START verb is `$1` when it is a declared verb. The START slug is `$2` when it matches the grammar
  `check_slug` enforces at `tools/unattended/unattended.sh:1060-1070`, a letter followed by letters,
  digits or dashes, with no length bound, as at base. The shape test is factored out of `check_slug`
  into one predicate both call, so there is no second grammar. END reads the verb and slug START
  captured from `$1` and `$2` at install, each set once, so the two lines cannot disagree. The parsed
  `VERB` is not used: the `--phase` arm exits inline before anything assigns it. END reads every other
  variable as `${NAME:-}` because the driver runs under `set -u`. The unit field comes from
  `BR_UNIT` for `--brief`, `PK_ITEM` for `--dispatch` and `--rescope` only, and `RV_SUBJECT` for
  `--review`. `PH_SLUG` is never read, because END takes the slug START captured. A call whose first
  argument is not a declared verb is journaled with an empty verb and slug, since its `$2` is then a
  flag's value and not a slug. `PK_ITEM` is also the free-text item of `--park`,
  `--propose` and `--attest`, so it is never read for those. `unit` is written only when the value
  matches the unit-id shape `_ids_of` greps for; otherwise `unit_bad=1` is set, and an empty value
  writes neither.
- `GOV_RUNLOG` is read BEFORE the conf is sourced, so the switch is the environment's: a tracked conf
  the run commits itself does not turn its own log off by assigning it.

### Why no signal traps

A trapped signal waits for the running foreground child. Measured on node `d` by the round-1 audit, TERM
ended an untrapped script running `sleep 4` in 0.33 s, and one with `trap 'exit 143' TERM` in 4.05 s.
The driver runs `$GATE_CMD` in the foreground under `GATE_BOUND`, which defaults to 3600 s. A TERM trap
would therefore hold a killed `--close` for up to an hour. The clean-exit marker records the same fact,
killed or chosen, with no change to how the driver dies. The price is that an unclean END carries the
`$?` the trap saw, often 0, so the model reads `exit=unclean` and never `rc` alone.

### Pure-bash resolution

| value | how, with no fork |
|---|---|
| time | `${EPOCHREALTIME/,/.}`, since the radix is locale-dependent; fallback `printf -v t '%(%s)T' -1` on bash 4.x |
| git dir | `$ROOT/.git` is a directory, or a file read with `read -r` for its `gitdir:` line |
| common dir | `<git-dir>/<commondir contents>` when that file exists, else the git dir itself, which is the primary tree's case |
| phase | a `while read` over RUN.md into a variable, never `$(fact …)`, which forks |
| duration | integer microseconds from the two `EPOCHREALTIME` values |

The stamp lives in the per-worktree git dir as `runlog-stamp-<slug>`, and END updates it with `: >`.
A `-nt` comparison is mtime-based. So `oob=1` also fires after a checkout, merge or stash rewrote
RUN.md. The flag means "changed outside the driver since its last logged call", and §5 names it as
noise to be read, not an accusation.

### Data model

START: `v t p=driver ev=start n verb slug wt kit pid phase_from oob sess.<NAME>...`. END: `v t
p=driver ev=end n verb slug unit rc exit checks phase_to dur_us`. The nonce `n` is `<pid>.<EPOCHREALTIME
digits>`. `checks` joins the numbers with commas and is written empty when nothing refused;
`phase_from` and `phase_to` are empty when RUN.md is absent or names no phase. A START carries at
most 8 session fields. The slug, the worktree path and the phase are UNBOUNDED, so "well under the
cap" is not a construction: a line over 2048 bytes is fitted by the runlog kit's reference rule. The
driver writes no indexed family, so only the value cut applies, and the suite compares its output
with `render_line` byte for byte, on an ASCII value and on one whose cut lands inside a character.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `write_runlog_start`, `write_runlog_end`, `write_runlog_line`, `read_phase_into`, `resolve_runlog_dirs`, `check_slug_shape` | shell functions | `sh.function`, snake_case, verb-led |
| `RUNLOG_SESSION_VARS` | conf key, `[A-Z_]` only as check 22 requires | protocol section 8 |
| `GOV_RUNLOG` | environment switch | none |

### Files touched (estimate)

`tools/unattended/{unattended.sh,.unattended.conf.example,PROTOCOL.template.md,VERBS.template.md,kit.toml,runlog-writer.test.sh}`,
`.unattended.conf`, `memory/guides/UNATTENDED-{PROTOCOL,VERBS}.md`, the 15 version carriers,
`tools/run-gates/selftest-budgets.txt`, three `memory/gotchas/` records with their index and dossier
claims, and the regenerated map.

### Alternatives rejected

- One END-only line: rejected because a killed call would leave nothing. Measured: KILL leaves no trap
  line, and TERM's trap sees `$?` of 0.
- TERM, HUP and INT traps: rejected by the deferral measured above.
- Two `git hash-object` calls per verb for out-of-band detection: rejected by S8's budget, at about
  40 ms each on node `d`.
- Logging the refusal text: rejected because it is free text carrying paths, and the check number
  plus the transcript, where local, answer the same question.

## 5. Production-readiness checklist

- security — the slug is used in a path only after it passes `check_slug`'s grammar. Session values
  are shape-checked before they are written. The conf can still `exit` before the trap is installed,
  which is recorded as a known hole in the writer's header, as charter §7 requires.
- perf / scale — zero added spawns on the hot path (AC7). About two appends of under 1 ms each per call.
- error / empty / loading states — an unwritable or absent journal gives one stderr line and an
  unchanged exit code. An absent RUN.md gives an empty `phase_from`. No stamp gives no `oob`.
- observability — the killed-call signatures are a START with no END, or an END with `exit=unclean`.
  `checks=` names every refusal.
- risks — `oob` false positives after git operations, disclosed in §4. A future driver exit that
  bypasses the marker, which the suite's enumeration arm guards.
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
  checks=14` and a `phase_to` read from the file, all with `exit=clean`. Over the whole journal the
  suite writes, every END nonce has a START, and every END's verb equals its START's.
  Red when: `fail()` stops recording checks, `phase_to` is taken from `rc`, an END is unpaired, or the
  `--phase` END carries an empty verb.
- **AC2** — When a verb exits through each shell exit shape the driver has, END reads `exit=clean` with
  `rc` equal to the process exit status. The shapes are `exit "$status"`, an inline `--phase` exit and
  a usage error. A sandbox conf that sets its own `trap 'exit 0' EXIT` changes neither. The suite also
  enumerates every `exit` in `tools/unattended/unattended.sh` and `tools/unattended/lib-unattended.sh`
  by §4's rule, with §4's five exemptions, and fails on one with no clean-exit marker. The enumeration
  is staged RED with an unmarked `exit` inside a verb body above the install line, and with one in
  `lib-unattended.sh`. Observed with `bash <suite>`.
  Red when: the trap is installed after the argument loop, or before the conf source, or an exit site
  anywhere in either file loses its marker.
- **AC3** — When `--close` runs in the sandbox with `GATE_CMD` set to a stub that writes a ready file
  as its first act and then sleeps 20 s, and the driver is sent TERM only after that file appears,
  checked with a bounded poll that also asserts the stub is still running, its END reads
  `exit=unclean` and the driver has exited before the stub's 20 s would have elapsed. When a verb is sent KILL, its START stands alone and the nonce has no
  END.
  Red when: a TERM trap is added, so the driver outlives the signal until the child returns, or the END
  reads `exit=clean`.
- **AC4** — When RUN.md is edited by a plain write between two verbs, the second START carries `oob=1`.
  When nothing touched it, and on the first call for a slug with no stamp yet, the key is absent.
  Red when: the stamp is not refreshed at END, or a missing stamp reads as `oob=1`.
- **AC5** — With `RUNLOG_SESSION_VARS` naming a variable set to a UUID and one set to a value holding
  `/`, the START carries `sess.<NAME>=<uuid>` for the first and `sess_bad=1` for the second.
  Red when: an unvalidated value reaches the line.
- **AC6** — When `--version` and `--plan <slug>` run, no line is written. When `GOV_RUNLOG=0` is set,
  no verb writes a line.
  Red when: either exclusion is dropped.
- **AC7** — When `bash -x` traces `--status dLoggedFlight` with `PS4='+ ${EPOCHREALTIME} '` on this
  worktree before and after the unit, with the journal directory already present, the external-exec
  count is identical. The trace goes to its own descriptor through `BASH_XTRACEFD`, because a trace
  on stderr goes blind inside every function called with `2>/dev/null`. That before-and-after pair is
  observed once, in the ledger, since the "before" driver does not outlive this unit; the suite's arm
  is its perpetual form, tracing `--status` in its sandbox with `GOV_RUNLOG=0` and with the writer on.
  Red when: the writer adds a `date`, `git` or `mkdir` call to the hot path.
  figure: the count is DERIVED at observation time and moves with RUN.md, because `--status` hashes
  each briefed unit's file. On 2026-09-13 it read 15 and then 17, before and after this unit's own
  `--brief` row, with the trace on its own descriptor. Traced on stderr, the 15 read as 12.
- **AC8** — When the journal directory is a file, so the append fails, the verb's exit code and stdout
  are unchanged and stderr carries one `unattended: run log` line.
  Red when: the write failure changes `rc` or prints to stdout.
- **AC9** — When `bash <suite>` runs, it passes at or above its
  `FLOOR_ASSERTIONS`, prints `PASS (<n> assertions)` and finishes inside its budget row.
  `tools/gate-legs.json` names no `tools/unattended/*.test.sh`, and the suite is in the
  `project-owned` include of `tools/unattended/kit.toml`.
  Red when: the suite is unbudgeted, under its floor, appears as a manifest leg, or ships to adopters.
- **AC10** — When `bash tools/unattended/adopt-unattended.sh --check` and `bash tools/check-kit-versions.sh`
  run, both are green with the protocol and verbs copies byte-identical to their templates at 1.20,
  and check 22 of `tools/unattended/check-unattended.sh` accepts the new key. An anchored `grep -n` finds
  the run-log paragraph in section 2 of `memory/guides/UNATTENDED-PROTOCOL.md` and the preamble
  sentence in `memory/guides/UNATTENDED-VERBS.md`.
  Red when: the section 8 row or the example line is missing, or the paragraph or sentence is absent
  from both copies, which byte identity alone would pass.
- **AC11** — When the suite runs a verb from a linked worktree of its sandbox and from the sandbox's
  primary tree, both lines land in `<common-dir>/runlog/driver.log`.
  Red when: the linked worktree writes under `.git/worktrees/`, or the primary tree finds no journal.
- **AC12** — When `python tools/memory-tree/gotchas.py --for-paths tools/unattended/unattended.sh`
  runs, it selects all three new gotcha classes.
  Red when: a record is unregistered or unanchored.
- **AC13** — When `--brief`, `--dispatch`, `--rescope` and `--review` each run with a unit-id argument,
  and `--phase` runs with a slug, each END carries that value in `unit` or `slug`. When
  `--park --item "<free text>"` runs, no line contains the item text. When a unit-bearing verb is given
  a value that is not unit-shaped, its END carries `unit_bad=1`. Over a fixed probe set, `--brief`
  writes `unit` exactly where the ERE read from `_ids_of`'s own line matches the probe.
  Red when: `PK_ITEM` is read for a free-text verb, an unset variable aborts the trap, or the
  writer's unit shape and `_ids_of`'s grammar disagree on a probe.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `kit version markers` · `harness arms (fail branches armed or pinned)` · `every held leg is budgeted, every budget row resolves` · `govkit selfcheck` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `shell hygiene (a loop fed by a command substitution)` · `gotchas selftest` · `memory hygiene`

New arm: `tools/unattended/runlog-writer.test.sh` · each AC staged RED by removing the property it observes · floor set at landing

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · S1 S2 S5 S10 S12 · §4 · AC2 AC3 AC4 AC9 AC11 AC12 · folded round-1 spec audit
  B4 (the suite is withheld and budgeted, never a leg, per the 2026-08-23 ruling and
  TOOL-aQuenchedHarness-3), M18 (no signal traps; a clean-exit marker replaces them, because a trap
  defers a killed `--close` up to `GATE_BOUND`), M5 (no stamp means no `oob`), L1 (START's slug uses
  `check_slug`'s grammar through one shared predicate), H3 (a linked-worktree arm) and the two gotcha
  records the audit's left-shifts name.
- rev-3 · 2026-09-13 · S1 S12 · §4 · AC1 AC2 AC3 AC9 AC10 AC12 AC13 · folded round-2 spec audit M3 (the unit
  field reads `PK_ITEM` only for the verbs whose item is a unit, and every variable under `set -u`
  defaults), M12 (AC3's TERM waits on a ready file the stub writes), L4 (the exit enumeration spans
  both driver files), M13 (anchored presence greps for the carriers) and M1 (AC9 observes the
  withholding), with the pairing duty and a third gotcha record.
- rev-4 · 2026-09-13 · §4 · AC1 AC2 · folded round-3 spec audit M2 (AC2 grades §4's whole population,
  and `:5021` joins the marker list), M3 (END reads the verb START captured, since `VERB` is empty on
  the `--phase` path) and L4 (no 64-character bound, which `check_slug` never had).
- rev-5 · 2026-09-13 · S6 · §4 · AC7 · the build pass. S6 says what an unset variable, a bad name and
  a ninth name do, which rev-4 left to the writer. §4 drops the `PH_SLUG` read rev-4 made redundant,
  names the exemptions by text because the unit's own insertions move their numbers, reads
  `GOV_RUNLOG` before the conf, and adds `write_runlog_line`: the data model's "well under the cap"
  was false for an unbounded slug, path or phase, so the line is fitted by the runlog kit's reference
  rule and graded against it. AC7's trace moves to its own descriptor, since the stderr trace of this
  very call missed three execs inside `2>/dev/null` callees, and its before-and-after pair becomes a
  ledger observation with a perpetual on-and-off arm in the suite.
- rev-6 · 2026-09-13 · S10 · AC13 · the bug-class checklist over the build commit. S10 no longer
  says the suite never runs through `run-unattended-gates.sh`, which derives its population from
  the budget rows and so does run it. AC13 joins the writer's pure-bash unit shape to the ERE in
  `_ids_of`, because a second spelling of one grammar is the two-answers class and nothing compared
  them; the arm was staged RED from each side.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "append one line per driver verb invocation to a machine-local log"`
found no seam: the `.sh` layer is unscanned, and no shell writer in `tools/` appends a per-act line
today. The measured precedents are `park()` at `tools/unattended/unattended.sh:3911-3920`, which
appends with `printf >>` but forks `date`, and the gate runner's run record, which is written once
per run. This unit reuses the `printf >>` append and replaces the `date` fork with `EPOCHREALTIME`.
It reuses `check_slug`'s grammar rather than writing a second one. No existing seam fits the writer.
Rejected candidates and their tests are in the design research record.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
