# TOOL-aWokenSentinel-1 — the run-state file records the LEASE: `session:` and `pid:` at preflight, and `--resume --keepalive-id` replaces it

**Status:** SPECCED · rev-1 · 2026-09-16 · node a · Tier-2 · base 5f9648d6 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md](../build/2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md) | research | TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 |
| [2026-09-16-prompt-TOOL-aWokenSentinel-1-0-run-mandate.md](../prompts/2026-09-16-prompt-TOOL-aWokenSentinel-1-0-run-mandate.md) | journal | — |
| [2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md) | journal | TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing outside a session can find the session holding an unattended run: the record names a cron
job id and no session, so every out-of-session actor this build adds — the stop-guard, the
stall-recorder, the resume tick — would have nothing to bind to. `tools/unattended/unattended.sh`
records two more facts at `--preflight`, `session:` from `CLAUDE_CODE_SESSION_ID` and `pid:` from
`CLAUDE_PID`, and `--resume` gains `--keepalive-id <id>` so a resumed session re-records all
three and the record stops saying it "cannot be corrected in place". Tier 2 by the manifest's rule:
the run-state file is the kit's contract and this changes what it carries.

## 2. Scope (IN)

- **S1** — `verb_preflight` records the lease directly after `set_fact "$rel" keepalive "$kid"`:
  `session: <CLAUDE_CODE_SESSION_ID>` and `pid: <CLAUDE_PID>`, each the literal `absent` when its
  variable is unset or empty, with ONE stderr NOTE naming which is absent and that no out-of-session
  resumer can find this run. Observed by AC1 and AC2.
- **S2** — `--resume <slug> --keepalive-id <id>`: on a non-terminal record the driver re-records
  `keepalive`, `session` and `pid` through the same function S1 writes with, prints one line naming
  each old and new value, and stages the file through `stage_or_fail`; on a terminal record it
  refuses through `refuse_if_terminal` with `via --resume`. Without the option `--resume` is
  byte-identical to today. Observed by AC3 and AC4.
- **S3** — The three `set_fact` calls live in ONE function, `write_lease`, with two callers;
  neither verb carries its own copy. Observed by AC5.
- **S4** — The carriers that describe the authored region: the scaffold header `scaffold_runmd`
  prints into every new record names the lease; the driver's own comment in `verb_resume` that says
  the region "carries twelve facts" stops stating a count; section 2 of
  `tools/unattended/PROTOCOL.template.md` gains the two facts as items 14 and 15 of its numbered
  list, and its render `memory/guides/UNATTENDED-PROTOCOL.md` is re-made in the same commit.
  Observed by AC6.
- **S5** — The verb carriers for the widened `--resume`: the driver's header line reads
  `#   unattended.sh --resume <slug> [--keepalive-id <id>]`, the `--resume` bullet of
  `tools/unattended/VERBS.template.md` names the option and what it replaces, and the render
  `memory/guides/UNATTENDED-VERBS.md` is re-made in the same commit. Observed by AC7.
- **S6** — Arms in `tools/unattended/unattended.test.sh`, one per criterion below, each observed
  red on a staged break of the one line it grades; the suite's prologue pins
  `CLAUDE_CODE_SESSION_ID` and `CLAUDE_PID` to fixture values so no fixture record inherits the
  ids of whatever session runs the suite. Observed by AC1 to AC5.
- **S7** — The record obligations of the pass: this spec's header goes to CLOSED in the pass
  commit; the acceptance ledger at
  `memory/builds/aWokenSentinel/build/2026-09-16-build-TOOL-aWokenSentinel-1-1-acceptance-ledger.md`
  carries one row per criterion; `--dispatch` declares the write set section 4 lists. Observed by
  AC8.

## 3. Non-goals (OUT)

- **No reader of the lease.** This unit WRITES two facts. Who reads them — the liveness verb, the
  two hooks, the tick — is units 2 to 5, and each reads through `fact` and never writes.
- **No prose change to the Skill or to protocol section 5.** `tools/unattended/SKILL.template.md`
  still says at `## Resume` that the record cannot be corrected in place, and
  `tools/unattended/PROTOCOL.template.md` section 5 still says `--keepalive-id` is accepted by
  `--preflight` alone. Both sentences become false at this unit's commit and are rewritten by
  `TOOL-aWokenSentinel-6`, which greps every carrier for them; this unit touches section 2 only,
  because that section enumerates the facts and would otherwise say "nothing else" over a record
  carrying two it does not list.
- **No `--status` line for the lease.** `--status` is a human line and gains a resume-tick line in
  unit 5 and a keepalive-listing line in unit 7; a lease line there would be a third edit to one
  printf by three units.
- **No re-preflight route.** `TOOL-aBranchedMandate-8` records that `--preflight` on a live record
  overwrites it and re-pins the anchor; that is why the replacement rides `--resume`, and this unit
  does not touch `verb_preflight`'s live-record behaviour.
- **No new `fail` branch.** The terminal refusal is the existing check 26 of `refuse_if_terminal`;
  the absent-id case is a NOTE, not a refusal, because a harness that exposes no id is a fact about
  the harness and a run under it must still start.
- **No kit version bump, no `ARMS_FLOORS` raise.** The closing pass bumps unattended 1.24 to 1.25
  once. `python3 tools/memory-tree/check-arms.py --report` at base reads the driver as
  `branches 201 (floor 104)   armed 194 (floor 101)`; this unit adds no branch, so neither floor
  moves.
- **No dossier edit.** `memory/map/features/unattended.md` sits at 20387 of 20480 bytes, PINNED
  2026-09-16; unit 6 refreshes its prose for the whole build, and this unit adds no inventory key
  the map enumerates — a conf key and a run fact are not key classes of `map_extractors.py`.

### Edges

- **consumes-from** external — `CLAUDE_CODE_SESSION_ID` and `CLAUDE_PID` in a session's Bash
  environment, measured present on node `a` on 2026-09-13 and again on 2026-09-16 (this spec's
  own probe: the session id equals the transcript uuid and the pid names a live `claude.exe`). A
  sub-agent sees the PARENT's session id. A harness that exposes neither records `absent` and
  the run starts anyway.
- **hands-off** `TOOL-aWokenSentinel-2` — reading `session:` and `pid:` through `fact`, and
  reporting a record whose session is `absent` as `UNBOUND`.
- **hands-off** `TOOL-aWokenSentinel-3` — binding a hook's stdin `session_id` to the run whose
  `session:` fact equals it; an `absent` fact binds nothing.
- **hands-off** `TOOL-aWokenSentinel-4` — the same binding from the stall-recorder, through the
  module unit 3 extracts.
- **hands-off** `TOOL-aWokenSentinel-6` — the `## Resume` prose of the Skill, protocol section
  5's "accepted by `--preflight` alone", and the dossier prose.
- **hands-off** `TOOL-aWokenSentinel-7` — reading the `session:` fact when `--landed` joins the
  last stop line to the run.
- **hands-off** external — the kit version bump across every carrier
  `bash tools/check-kit-versions.sh` names, the closing pass's, once.

## 4. Design

### The lease, written by one function (S1, S3)

A new function `write_lease` in `tools/unattended/unattended.sh`, placed beside `set_fact`
at `:2876`, signature `write_lease <run-state file> <keepalive-id>`. `write` is a declared verb of
`.lexicon.conf` and `python tools/lexicon/lexicon.py --suggest write_lease --as sh.function`
answers OK, so the lexicon offender pin does not move. Body:

1. `set_fact "$rel" keepalive "$kid"` — the line `verb_preflight` carries today at `:2805`, moved.
2. `sid="${CLAUDE_CODE_SESSION_ID:-}"`, `pid="${CLAUDE_PID:-}"`; each empty one becomes the
   literal `absent`.
3. `set_fact "$rel" session "$sid"`, `set_fact "$rel" pid "$pid"`.
4. When either was empty, ONE line on stderr: `unattended: NOTE - this harness exposes no
   <session id|pid|session id or pid>, so no out-of-session resumer can find this run; the lease
   records absent and the hooks and the tick report it UNBOUND rather than guess.` The
   alternation is filled by which was empty; the sentence is emitted once per call.

`verb_preflight` at `:2805` calls `write_lease "$rel" "$kid"` in place of its `set_fact` line. The
`absent` literal rather than an omitted key: a reader keyed on the KEY's presence would read a
pre-1.25 record and an unexposed-harness record alike, and those are different facts — one was
never asked, the other was asked and answered no. `fact` returns the literal, so every reader
tests one string.

The pid is recorded as handed. On node `a` it is the Windows pid of `claude.exe` (`tasklist` shows
it; `kill -0` on it fails under MSYS even while it lives, measured 2026-09-16), which is unit 2's
problem to probe and this unit's to record verbatim.

### The replacement on resume (S2)

The option parser at `:5235` already binds `--keepalive-id` into `KID` for EVERY verb; only
`verb_preflight` receives it, at the dispatch `case` line `:5322`. So the brief's "extend the
parser to `--resume`" is one word: the dispatch arm at `:5325` becomes
`--resume) verb_resume "$SLUG" "$KID" ;;` and no parser changes. `verb_resume` at `:3079` takes
the optional second positional:

- Terminal phase, option given: `refuse_if_terminal "$rel" --resume || return 1` before the
  "nothing to resume" lines, so the refusal is the whole output. The sentence is check 26's
  existing one, ending `: <phase> via --resume`. Terminal phase, no option: unchanged.
- Non-terminal phase, option given: after today's resume lines, read the three old values through
  `fact`, call `write_lease "$rel" "$kid"`, print
  `unattended: lease replaced · keepalive <old> -> <new> · session <old> -> <new> · pid <old> -> <new>`,
  then `stage_or_fail "$rel" || return 1` — the staging `--park` uses at `:1658`, so the new lease
  is in the index the gate leg reads. The NOTE fires here too when the resumed session's harness
  exposes no id.
- Non-terminal phase, no option: unchanged. An empty `--keepalive-id ""` is indistinguishable from
  the option's absence at the parser and behaves as absence.

Why the resumed session must call this and not `--preflight`: `TOOL-aBranchedMandate-8`, and the
Skill's own `## Resume` paragraph, which says re-preflighting "refuses on a dirty tree and re-pins
the anchor". The Skill's next sentence, that the record cannot be corrected, is what this unit makes
false and unit 6 deletes.

### The carriers (S4, S5)

- `scaffold_runmd` at `:1630`: the third and fourth `printf` lines read `only what nothing else
  does: the phase and its witness, the keepalive id and the lease — the session and pid holding
  the run — the pinned BASE with its anchor evidence, and the parked decisions.` Records already
  on disk keep their old header; nothing grades it.
- The comment at `:3092` in `verb_resume` — `the authored region carries twelve facts and never
  restates a derivable one` — becomes `carries the facts protocol section 2 enumerates and never
  restates a derivable one`. The brief expected the count in the protocol; at base the protocol's
  section 2 already says `NO COUNT IS WRITTEN HERE` and this comment is the one carrier that still
  types one.
- `tools/unattended/PROTOCOL.template.md` section 2, after item 13: item 14, **the session id**
  holding the run, from `CLAUDE_CODE_SESSION_ID` at `--preflight`, re-recorded by `--resume
  --keepalive-id`, the literal `absent` where the harness exposes none; item 15, **the pid** of the
  process holding the run, from `CLAUDE_PID`, on the same terms. The paragraph beginning `Facts
  10, 11 and 12 are ABSENT` gains one sentence: facts 14 and 15 are always WRITTEN, and the literal
  `absent` is a value, not a missing line. Render with `bash tools/unattended/adopt-unattended.sh`.
- Header line `:10` of the driver: `#   unattended.sh --resume <slug> [--keepalive-id <id>]  # the
  same line, plus the next action; with the id, the lease is replaced`. Check 26 of the kit gate
  matches the header by the prefix `#   unattended.sh --resume `, so the widened line still joins.
- `tools/unattended/VERBS.template.md`, the `--resume` bullet: `re-enters the run from the
  run-state file; must agree with --status. With --keepalive-id <id> it REPLACES the lease —
  keepalive, session, pid — so a resumed session's record names the session that now holds it;
  refused on a terminal record.` Render with the same adopter run.

### The fixture (S6)

The suite's prologue, directly after `export GOV_DEFAULT_BRANCH=main` at
`tools/unattended/unattended.test.sh:352`, exports `CLAUDE_CODE_SESSION_ID=fixture-session` and
`CLAUDE_PID=999999999`. Every existing `--preflight` in the suite then records a lease that is the
same on every box and names no live process — `memory/gotchas/fixture-inherits-ambient-machine-state.md`
is the class; the bar runs inside a Claude session on every registered node and would otherwise
stamp each fixture record with that session's real id. The pid value is above any pid a Linux
box hands out and no Windows box on this fleet has reached; unit 2's `pid-alive: no` arm sets its
own impossible value by `mutate` rather than trusting this one.

The unit's own arms, in a new block beside the `--audit` arms in region two:

1. `reset_tree`, then `CLAUDE_CODE_SESSION_ID=abc CLAUDE_PID=4242 bash "$SCRIPT" --preflight tRun
   --keepalive-id k1` — the fixture's `run` helper is not used because the env is the subject.
2. `reset_tree`, then `env -u CLAUDE_CODE_SESSION_ID -u CLAUDE_PID bash "$SCRIPT" --preflight tRun
   --keepalive-id k1 2>&1`.
3. On the record arm 1 left: `run --resume tRun --keepalive-id zzz`.
4. `mutate` the phase to `LANDED`, then the same invocation.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `write_lease` | shell function in `unattended.sh` | `sh.function`, verb `write` |
| `session`, `pid` | run-state facts, written by `set_fact` | not a naming cell; the key grammar is `set_fact`'s own |

### Rollout

The pass declares, through `--dispatch --writes`: `tools/unattended/unattended.sh`,
`tools/unattended/unattended.test.sh`, `tools/unattended/PROTOCOL.template.md`,
`memory/guides/UNATTENDED-PROTOCOL.md`, `tools/unattended/VERBS.template.md`,
`memory/guides/UNATTENDED-VERBS.md`, this spec, the build README, the acceptance ledger S7 names,
and the generated `memory/LIVE.md` and `memory/ledger/2026-09.md`. No path on the manifest's
`watch` line moves, so no `last-audit` re-stamp is owed.

Forward-compatible: a record written before this unit carries neither key and every reader treats
a missing key exactly as `absent`; a record written after it is read by a pre-1.25 driver, which
ignores keys it does not ask for. No migration.

The one check the pass verifies with is the four driver invocations of section 6 over the fixture,
each once against the built driver and once against a copy with its graded line removed.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/unattended/unattended.sh` | `write_lease` added; `verb_preflight` calls it; `verb_resume` takes the id; dispatch arm passes `$KID`; header line, scaffold text and one comment |
| `tools/unattended/unattended.test.sh` | two prologue exports; one arm block |
| `tools/unattended/PROTOCOL.template.md` | section 2 items 14 and 15, one sentence |
| `memory/guides/UNATTENDED-PROTOCOL.md` | re-rendered |
| `tools/unattended/VERBS.template.md` | the `--resume` bullet |
| `memory/guides/UNATTENDED-VERBS.md` | re-rendered |

### Alternatives rejected

- **Omit the key when the variable is unset.** A missing line and a pre-1.25 record are the same
  bytes; `absent` is a recorded answer and a missing line is an unasked question.
- **A `--lease` verb of its own.** Check 26 would owe it a header line, a VERBS bullet and a Skill
  invocation, for an act that only ever happens on resume; the Skill's `## Resume` already tells a
  resumed session to run `--resume` first.
- **Record `CLAUDE_CODE_HOST_SESSION_ID` too.** It is the desktop app's `local_…` id, measured
  distinct from the transcript uuid; no reader in this build resolves anything through it, and a
  third key with no consumer is the two-answers class waiting for its second answer.
- **Re-record the lease on every verb.** A verb run from a second session — an owner's `--status`
  over a live run — would overwrite the lease of the session doing the work; only the two acts that
  START holding a run write it.

## 5. Production-readiness checklist

- security — the lease is written by the run's own driver into a file the run already authors;
  a forged `session:` binds the hooks to a session that is not holding the run, which is the trust
  level of every authored fact and is why unit 2 reports rather than acts on it. No new input
  crosses a trust boundary: the values come from the harness's environment, not from argv.
- perf / scale — two `set_fact` calls, each one `awk` pass over a file capped by the index cap;
  milliseconds on the two verbs that already rewrite the record.
- error / empty / loading states — an unset variable is `absent` plus a NOTE; a terminal record
  with the option is a named refusal; an empty option value is the option's absence.
- observability — the replacement line prints all six values so a resumed session's transcript
  shows what the record said before and after; the NOTE names which id the harness withheld.
- risks — a harness that exposes a session id that is NOT the transcript uuid would bind the
  hooks to nothing; measured equal on node `a` only, so an adopter on another harness reads
  `UNBOUND` or a mismatch, never a false `LIVE`. Moving the keepalive `set_fact` into a function
  changes no bytes it writes; the existing `keepalive:` arms stand.
- testing — section 6; every arm runs the driver over the fixture. The suite is on no bar leg and
  is not run inside the pass.
- migration — N/A. Old records read as `absent`; the key set is additive.
- user docs — the verb carrier and protocol section 2 are the docs, rendered and byte-compared
  by the kit gate; the Skill prose is unit 6's.

## 6. Acceptance criteria

The suite that carries the arms is on no bar leg — `tools/unattended/kit.toml` records the
2026-08-23 ruling — and the build's rule three keeps it out of the pass. Each criterion is observed
by running the driver over the suite's `tRun` fixture in a scratch clone, exactly as its arm does,
after `reset_tree`; the arms exist so `harness arms (fail branches armed or pinned)` counts them at
the close. The staged break for each is a copy of the driver with the named line removed, run by
the same invocation.

- **AC1** — When `CLAUDE_CODE_SESSION_ID=abc CLAUDE_PID=4242 bash tools/unattended/unattended.sh --preflight tRun --keepalive-id k1`
  runs over the fixture, `grep -c '^session: abc$'` and `grep -c '^pid: 4242$'` over the fixture's
  run-state file each print `1`, `grep -c '^keepalive: k1$'` prints `1`, and stderr carries no
  `NOTE - this harness exposes no` line.
  Red when: either count is `0`, which is the lease not written or written under another key; the
  keepalive count is `0`, which is the moved line lost; or the NOTE fires with both variables set.
  fixture: the suite's scratch repo; no live fixture in this tree.
- **AC2** — When `env -u CLAUDE_CODE_SESSION_ID -u CLAUDE_PID bash tools/unattended/unattended.sh --preflight tRun --keepalive-id k1`
  runs over a reset fixture, `grep -c '^session: absent$'` and `grep -c '^pid: absent$'` each print
  `1`, and the merged output carries `NOTE - this harness exposes no session id or pid, so no
  out-of-session resumer can find this run` exactly once.
  Red when: a key is missing rather than `absent`; the NOTE is absent, or prints twice, which is
  one NOTE per variable rather than one per call.
- **AC3** — When, on the record AC1 left, `bash tools/unattended/unattended.sh --resume tRun --keepalive-id zzz`
  runs with `CLAUDE_CODE_SESSION_ID=def CLAUDE_PID=9`, the output carries `resume at phase
  RUNNING` and the line `lease replaced · keepalive k1 -> zzz · session abc -> def · pid 4242 -> 9`,
  the three greps of AC1 with the new values each print `1`, `git diff --cached --name-only` lists
  the run-state file, and the exit is 0; and when `bash tools/unattended/unattended.sh --resume tRun`
  runs without the option, the output carries no `lease replaced` line and the record's three
  values are unchanged.
  Red when: the replacement line is absent or names the wrong old values, which is the read
  happening after the write; the file is not staged; or the plain form rewrites the lease.
- **AC4** — When the fixture's phase is rewritten to `LANDED` by `mutate` and
  `bash tools/unattended/unattended.sh --resume tRun --keepalive-id zzz` runs, the output carries
  `UNATTENDED check 26 FAILED` and `LANDED via --resume`, no `lease replaced` line, the exit is 1,
  and `grep -c '^keepalive: zzz$'` prints `0`; and when the same terminal record gets
  `bash tools/unattended/unattended.sh --resume tRun` without the option, the output carries
  `nothing to resume — phase LANDED is terminal` and exits 0, which is the arm at
  `tools/unattended/unattended.test.sh:4370` still holding.
  Red when: a terminal record's lease is rewritten; the refusal names another verb; or the plain
  form starts refusing.
- **AC5** — When `grep -c 'write_lease' tools/unattended/unattended.sh` runs it prints at least
  `3` — one definition, one call in `verb_preflight`, one in `verb_resume` — and prints `0` at base;
  and `grep -cE 'set_fact "\$rel" (session|pid) ' tools/unattended/unattended.sh` prints exactly
  `2`, both inside the function.
  Red when: the first count is `2`, which is one verb keeping its own copy; or the second exceeds
  `2`, which is a third writer of the lease.
  figure: `3` and `2` are DERIVED by the grep at observation time.
- **AC6** — When `grep -c 'carries twelve facts' tools/unattended/unattended.sh` runs it prints
  `0` and prints `1` at base; `grep -c 'the session and pid holding the run' tools/unattended/unattended.sh`
  prints `1`; and `grep -cE '^1[45]\. \*\*The (session id|pid)\*\*'` over
  `tools/unattended/PROTOCOL.template.md` and over `memory/guides/UNATTENDED-PROTOCOL.md` each
  print `2`. Leg half, observed at `--close`: `bash tools/unattended/check-unattended.sh` byte-compares the protocol
  template to its render under its check 10.
  Red when: the count survives; the scaffold sentence is unchanged; either file lists one item or
  none; or the two files differ, which is a template edit without the render.
- **AC7** — When `grep -c 'unattended.sh --resume <slug> \[--keepalive-id <id>\]' tools/unattended/unattended.sh`
  runs it prints `1` and prints `0` at base; `grep -c 'REPLACES the lease'` over
  `tools/unattended/VERBS.template.md` and over `memory/guides/UNATTENDED-VERBS.md` each print `1`;
  and `bash tools/unattended/unattended.sh --version` still prints `unattended 1.24`, which is the
  version bump not taken here.
  Red when: the header line is unchanged, so `usage` still shows a `--resume` that takes no id; the
  bullet is absent from either file; or the version moved in this unit.
- **AC8** — When `git show --name-only --format= HEAD` runs on the pass commit, it lists none of
  the ten paths on the `watch` line of `memory/guides/SESSION-KICKOFF.md`, and
  `git grep -lE '^\*\*Status:\*\* CLOSED' -- memory/builds/aWokenSentinel/spec/` lists this spec.
  Red when: the commit lists a watched path, which means this pass touched something outside its
  declared set; or the header still reads `SPECCED`.
  figure: ten is what the `watch` line held on 2026-09-16; the observation reads the line, not
  this number.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness`

These are `--close`'s. The pass runs none of them: it verifies with the four driver invocations of
AC1 to AC4 over the fixture and the greps of AC5 to AC7, nothing else. Under `unattended kit gate`,
checks 10 and 26 are the joins this unit moves. Chunks read from `tools/gate-legs.json` on
2026-09-16: `unattended kit gate`, `harness arms`, `spec tokens`, `lexicon` and `codebase-map` are
`chunk: declarations`; `unattended skill wiring` is `chunk: wiring`; `install-prefix` is
`chunk: product`; `memory hygiene` is `chunk: records`; none is `chunk: selftests`.

New arm: `tools/unattended/unattended.test.sh` · the four invocations of AC1 to AC4 over the
`tRun` fixture, each red against a driver copy missing the graded line — the `session` write, the
`pid` write, the NOTE, the `$KID` pass-through at the dispatch arm, the `refuse_if_terminal` call
· `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` rise by the block's executed assertions; `FLOOR_SHARD_1`
does not move.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, from the brief in
  `memory/builds/aWokenSentinel/prompts/2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md`
  and the research record under `build/`. Two corrections against source: the option parser is
  already global, so the dispatch arm changes and the parser does not; and the "twelve facts" count
  lives in the driver's comment at `:3092`, not in the protocol, which already refuses to state one.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "record the session id and pid holding an unattended run
in the run-state file at preflight and resume, and re-record the keepalive id on resume"`, run on
2026-09-16 at base `5f9648d6`, reported `scan coverage: 73 files scanned | 0 parse skips |
unscanned layers: .sh` and ranked nothing in the driver, because the driver is shell and the map
does not scan that layer — `memory/gotchas/` records this blind spot, so the seam is cited from
source by grep. The seam this unit extends is `set_fact` at `tools/unattended/unattended.sh:2876`,
the writer every run fact goes through, and `verb_preflight`'s existing `set_fact "$rel"
keepalive "$kid"` at `:2805`, which becomes the first line of `write_lease`; the staging seam is
`stage_or_fail` at `:1658`, `--park`'s. The option is already parsed at `:5235` into `KID` for
every verb, so the second caller costs one word at the dispatch `case`. No existing function writes
a session or pid anywhere in `tools/`: `grep -rn 'CLAUDE_CODE_SESSION_ID\|CLAUDE_PID' tools/
skills/` over shipped files prints nothing at base.

The recall probe's live hits were `TOOL-aBranchedMandate-8` (OPEN: `--preflight` overwrites a live
record, which is why the replacement rides `--resume`), `TOOL-aPromptedMandate-11` (the
attestation unit 7 closes), and the protocol's section 5 line that `--keepalive-id` is accepted by
`--preflight` alone — TRUE at base as a statement about which verb receives the value, and STALE
as a statement about the parser, which binds it for every verb; unit 6 rewrites the sentence.

Recall terms used: `python tools/memory-recall/query.py "how does a resumed unattended session
record its replacement keepalive id, and what does the run-state file record about the session
holding the run" --terms "keepalive id record preflight resume run-state fact session pid lease
replacement cannot be corrected in place"`.
