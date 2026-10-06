<!-- gov:kit unattended@1.83 -->
# Unattended runs — the verbs

*This file is the second half of the binding contract; `UNATTENDED-PROTOCOL.md` is the first. Two
legs byte-compare it against the template it ships from. **They compare the two copies to each
other, so a claim FALSE IN BOTH is green** — a parity leg is a copy check, not a truth check, and
only a reader grades a sentence against the code. This file was created by moving section 7 of the
protocol verbatim, and one bullet arrived carrying a sentence the same build then measured false.*

Every verb but `--version` and `--plan` also writes a START and an END line to the machine-local
run log `UNATTENDED-PROTOCOL.md` §2 describes, and no verb reads it.

- `--preflight` — asserts the authorization, pins the BASE, CREATES and stages the run-state file,
  records the keepalive id the agent hands it, and accepts `--waive <handle> --reason <text>` where no
  other verb does (`UNATTENDED-PROTOCOL.md` §10). It refuses on a dirty tree, on the default branch, and on an unwired repo. It
  OBSERVES the anchor from the remote rather than reading a local ref, and refuses when the remote
  does not answer or advertises no default branch of its own — failing closed there costs nothing
  real, since a run that cannot reach the remote cannot land on it either. It delegates wiring to the
  project's **check** mode, never the repairing one: that mode rewrites tracked bytes and sets git
  config, and the run's first act must not be the mode whose past over-firing this protocol cites.
  Where the project declares `GATE_PROFILE_CMD` it pins the bar's backstop, the runner's wall plus
  its queue bound plus a margin, as the `gate-backstop` fact, and it refuses a wall below the
  largest leg ceiling that profile reports. It resolves this node against `LANDING_NODES` at BASE
  and at the advertised tip, lander only where both list it and undeclared only where neither
  declares the key, prints `landing — lander`, `handoff` or `undeclared`, and records the first two
  as `landing`. A record `--settle` marked `abandoned` it retires like a finished one.
  Where `RUN_CLAIMS` is `on` it reads every run claim on the remote right after the anchor, lists the
  ones of OTHER slugs that are not terminal, and refuses at check 107 a live, held or unreadable claim
  another session holds on this slug; it takes over a stale or terminal one. Its own claim is written
  by compare-and-swap after every precondition and BEFORE the rotation and the scaffold, so a race it
  loses (check 108) or a write that does not complete (check 109) leaves the tree untouched.
  `UNATTENDED-STOPS.md` §7 is the contract; undeclared, the switch is `off` and one NOTE says so.
- `--phase` — writes a phase and its witness. Without it the vocabulary is decorative: only
  `--preflight` and `--close` ever wrote one, so every member between them entered the file only by
  hand-editing an artifact this kit calls generated.
- `--park` — writes a decision the run REFUSED to take: the question, the options seen, the reason.
  Refused on a terminal record, and with no run-state file: a park minted for a run that never
  started records nothing about a run. **A fork with no delegated resolver is parked THROUGH THE
  VERB, and the run continues.** Not noted in prose, not left for the wrap-up to notice: `--park` is
  what a gate reads. The run then carries on with the units that do not depend on that fork. Only
  when EVERY remaining unit depends on it does the run halt, with the fork-unresolvable code — a run
  that can still make progress on something else is not stuck, and stopping early spends an owner
  turn that was not needed. A park that is not a no-op REFRESHES first: it lists the commits on the
  advertised tip in neither BASE nor HEAD that touch the build's README or a declared write, and
  records `refreshed-at` — the tip and the count, `unlisted` for a tip this clone lacks, or
  `unobserved` — never refusing and never fetching.
- `--brief` — records WHAT a build pass was handed: the unit, and the hash of a TRACKED brief file,
  through `park()` as a `history` kind. `--status` reads it, grading each unit's LATEST row.
- `--propose` — writes a PROPOSAL: an amendment a run would make to the playbook it is following,
  joined to the step that provoked it. Nothing blocks on it, and it is not an edit: a run that
  rewrites the checklist it is graded by has no rules left. It reuses `--park`'s newline, separator,
  bypass and terminal refusals over the new step field, and its exact-line idempotence — with the
  step inside the identity, so one amendment at two steps is two rows.
- `--attest` — **the two agent-attested items have a VERB, and it is the only way to write one.**
  `--attest <slug> --item <item> [--value <text>]` derives the record key so no operator spells
  one, and REFUSES a machine-checked item by reading its declared CHECKER — so a project
  declaring its own agent-attested extra gets the verb and one renaming a machine item gets the
  refusal. Before it existed the keys had no writer, which made `--abort` — the sole documented exit
  from a wedged run, requiring both — reachable only by hand-editing the authored region of a file
  this kit calls generated. The verb removes the hand edit, not the trust assumption
  `UNATTENDED-PROTOCOL.md` §9 states.
- `--record-piece` — writes one leg's verdict for one PIECE into a tracked record joined to that
  piece by content hash. It reuses `--park`'s newline, separator and bypass refusals and its
  exact-line idempotence. The writer takes a records ROOT rather than a slug, and `--records-root`
  reaches it BEFORE the slug and run-state checks — so the attended path calls the same function with
  no run at all, which is what makes it a second CALLER rather than a second implementation. Without
  that flag the verb resolves a slug and requires a run-state file. An earlier revision of this line
  called the verb "unattended-only", which contradicted its own first half and the code.
- `--record-set` — writes one leg's verdict for the WHOLE set of pieces, over an ordered hash list
  naming which pieces it covers. That population is the one a per-piece review structurally cannot
  see, and a verdict not naming its members cannot be re-checked.
- `--plan` — takes its unit SET and its ORDER from the GENERATED units region, which is why its
  "next" and `--status`'s are the same unit by construction rather than by coincidence. It prints
  each unit's id, status and the build method's M2 classification, and names the next one. It
  COMPUTES that vocabulary and does not define it; M2 does. It reads the SPEC FILES for two things
  the region cannot carry: that classification, and the two `NOT A UNIT` conditions, since a file
  with no parseable status header has no rendered row to appear in. A region that is absent OR
  malformed is a named refusal, never a fall-back to the older spec-derived listing. It still joins
  the build README's AUTHORED roster pair against the tracked specs, so a planned unit nobody has
  specced is reported as MISSING — that question cannot be answered from a region rendered out of
  the specs that exist. A trailing `--paths` swaps the padded table for TAB-separated rows carrying
  a FOURTH field, the spec path this verb already resolves per unit and otherwise discards, empty
  for a unit no tracked spec defines; the two `NOT A UNIT` diagnostics are keyed on a filename
  rather than an id and stay padded in both modes, so a caller splits on TAB and skips any line
  with fewer than four fields. The `roster:` and `next:` lines are unchanged, which is what makes
  one `--paths` invocation the resume path's single source for both "which unit is next" and "where
  is its spec".
  SEVERAL SLUGS may be given, and the single-slug form is then byte-identical to what it always
  was, because the framing appears only for two or more. Each build's output is opened by
  `unattended-plan-open: <slug>` and closed by `unattended-plan-rc: <slug> <rc>`, and each runs in
  its own subshell, so one build's refusal cannot colour the next and the caller still sees a
  per-build status it could otherwise not recover from a summary. It exists because this kit's own
  gate leg grades this verb's output across many builds, and one driver launch per build was the
  largest single item on the bar's longest leg.
  `--framed` asks for that framing at ANY arity, including one slug. It exists because deriving the
  format from the slug COUNT gives a caller two output shapes for one verb: a frame-reading caller
  handed a single-build corpus finds none of the lines it parses and reads the run as having graded
  NOTHING. Without the flag the one-slug form stays byte-identical to what it has always been.
- `--status` — ONE line, opened by `unattended: <slug>`, with every field after it joined by ` · `
  in the order this entry names them. The phase, the witness and the next unit print on every line:
  `phase <phase>`, where a LANDED an owner's hand-off made, derived or settled, reads
  `LANDED (attended)`, any other derived LANDED reads `LANDED (derived: <sha8> on <ref> at <tip8>)`,
  and a LANDING the derivation explains reads `LANDING (not on the remote: <reason>)`;
  `witness <sha>`, the sha reading `NONE` on a record that names none, which the verb then refuses;
  and `next <unit>`, the link label of the first non-terminal row in the generated units region, or
  `(no non-terminal unit)`. Every other field is OPTIONAL and prints only under the condition named
  beside it, so a record none of them applies to prints only the fields above. Between the witness
  and `next`: `halt-code <code>` when the record carries one, then `spec-audit <date>` when it pins
  one. After `next`, in order: `parked <n>` when owed parked rows exist; `noted <n>` when rows the
  owner is told of but owes no answer to exist; `STALE briefs <n>` when a unit's latest recorded
  brief no longer hashes the same, then `briefs gone <n>` when its file is gone; the resume tick's
  `resume-tick <n> attempt(s), last <stamp>` when its sidecar for this slug holds a line; and
  `orphans <n>` when the process ledger names one (`UNATTENDED-STOPS.md` §14, nothing killed). Then
  the two verdicts, the optional fields that print on a pass as well as on trouble, each on exactly
  the records whose `--resume` would run its check, because a report silent on a pass cannot be
  told from a verb that never asked. The pinned-asks verdict prints on every record that pins
  `asks`, a pass included, since `--resume` runs check 73 above every row of its matrix, and reads
  `asks as pinned` or
  `asks moved at HEAD, check 73 refuses a resume: pinned [<pin>] at HEAD [<now>]`. The
  holder-worktree verdict follows it, printing when the record carries `lease-utc`, its phase is not
  terminal and it is not a LANDING the landed log observed, which are the records on which
  `--resume` reaches check 58, a pass included, and reads `worktree holds the run`,
  `worktree not the run's, check 58 refuses a resume here: <where>`, or
  `worktree unanswerable, the record names no run branch`. Both read through the predicates the
  refusals use, so neither refuses anything here. LAST,
  `keepalive <id> present|absent in the harness listing at <utc>` from the stop-guard's newest
  sidecar line, whatever its phase, when the record names a keepalive id and that line exists. The
  line stays ONE line: a field joins it or does not print, and the suite arms that.
- `--audit` — one line per unit whose dispatch rows at their newest anchor, taken together, are still
  open and whose spec is not terminal: how long the TREE has been idle (newest write, newest commit) and `PROGRESSING` or `STALLED` against `UNIT_STALL_BOUND`, a
  `STALLED` line followed by one remedy line. Read-only; the idle-wake runs it. It cannot see what
  the unit is doing or whether a process is stuck — its figures are properties of the tree. After
  the units it prints one line per open REGISTERED task: its heartbeat path, `last-beat <s>s ago`
  or `none`, and `PROGRESSING` or `STALLED` against `TASK_STALL_BOUND`, a `STALLED` line again
  followed by one remedy line — or `no heartbeat-bearing tasks registered`. A heartbeat that exists
  and cannot be dated is check 51; one not written yet is graded from its registration.
- `--register-task` — `--register-task <slug> --task <name> --heartbeat <absolute path>`, run by
  the STARTER of a background task BEFORE it starts it: the main loop for an `Agent` or a background
  leg, a brief's author for a unit's own long command. It appends one row to the per-slug sidecar
  `tasks.<slug>.tsv` under `<git-dir>/unattended/`. A task beats by writing its heartbeat file; a
  leg or a suite beats by its own output log growing, so that log can be the path. It refuses a
  name or path carrying a tab or a newline, a relative path, a name still open, a missing run and a
  finished one. NOTHING ENFORCES IT: a background task nobody registers stays invisible to `--audit`.
- `--release-task` — `--release-task <slug> --task <name>`, when the task ends, so `--audit` stops
  grading it. A name with no open registration refuses; a released name may register again, and
  its newer row is the one graded.
- `--liveness` — key: value lines and one verdict for an OUT-OF-SESSION reader: the phase, the
  lease, whether the recorded pid exists AND is the leased process (image and start time, not the
  number alone), seconds since anything moved, the last recorded stall, `TERMINAL`, `ELSEWHERE`,
  `FINISHED-UNSTAMPED`, `HELD`, `UNBOUND`, `STALE` or `LIVE`, then the `stale-bound` it was graded
  against and the `holder-ref` a worktree must have checked out. Read-only; the stop-guard, the
  stall-recorder's readers and the resume tick call it rather than deciding for themselves. It
  cannot see what the session is doing or whether a process is hung — existence is not progress.
- `--resume` — re-enters the run from the run-state file; must agree with `--status`. With
  `--keepalive-id <id>` it applies the resume matrix: the holder's own id writes nothing, while a
  take-over, `--replaces`, the holder's restarted process and a pushed landing not yet observed
  re-record keepalive, session and pid and stage the record; refused on a recorded terminal, and on
  a record `--settle` marked `abandoned`, whose next run `--preflight` starts.
  Where `RUN_CLAIMS` is `on` the holder reads its claim on the remote on every call and renews it when
  due, a claim another session holds is check 108 for the holder and check 107 for a take-over, and
  `--replaces` and the landing re-bind write their new keepalive into it (`UNATTENDED-STOPS.md` §7).
  `--scheduled <held-at>` marks it as the restart a DURABLE schedule issued. It refuses, numbered
  and before any write, unless the exact hold that schedule was filed for is still the record's
  state, and on success the take-over runs unchanged, still requires the session's own
  `--keepalive-id`, and writes `scheduled` rather than `manual` on its history row.
  `UNATTENDED-STOPS.md` §8 and §11 are the contract.
- `--close` — evaluates the DoD set, blocks on any unmet item, records any override. The only writer
  of `LANDING`, and it runs BEFORE the landing it authorises, so it cannot observe one. Its bar is
  bounded by the pinned backstop, and `gates-green` names each other way a bar ends as what it is: a
  TREE MOVED exit is run once more, and a HOST exit or a kill before the bar acquired the repository
  prints a `hold ·` line rather than reading as a red leg. Under `primary` it prints `--park`'s
  refresh before the DoD and records `refreshed-at` only with a met DoD's writes. It resolves its own
  node again, at BASE before the anchor round-trip and at the advertised tip after it, and on a
  `landing` hand-off node it refuses any override and, with the DoD
  met, writes the bar's facts and refuses, naming `--handoff <slug> --code owner-landing`.
  Where `RUN_CLAIMS` is `on`, before any item is graded, a run that does not hold its claim
  on the remote is check 108 and a claim that cannot be read or renewed is check 109: a close
  that lands a claim it never read is a double landing.
- `--authorization` — `--authorization <slug>` grades `authorization-reachable` alone, by the arm
  `--close` grades it with, so it answers what the close would from the same tree. Run it after any
  merge of the remote's default branch into the run branch, mid-build included, and under
  `in-place` between the lander's `--prepare` and `--close`: a merged-in check can refuse a README
  pinned at BASE, and the close reads that item only after its bar. Met prints one
  `authorization-reachable — met` line and exits 0. A README refused at a derived BASE prints the
  numbered refusal, then one line naming the two exits — rotate by `--abort --code
  repo-state-out-of-mandate` and a fresh `--preflight`, or `--park` then `--handoff --code
  owner-decision` — and exits 1. A predicate that never reached the README, the anchor or the base
  derivation refusing, prints that refusal and `not evaluated` with no exits, and exits 2. It
  writes nothing to the tree, the record or the remote, and grades no other Definition-of-Done item.
- `--landed` — an OBSERVATION rather than a claim, guarded on the RECORDED phase. It accepts a record
  only at `LANDING` and re-observes the anchor. Under `primary` it is the one writer of `LANDED` and
  refuses unless HEAD is an ancestor of the tip the remote advertises; where `LANDER_MARKER` is
  declared it ALSO refuses unless the marker's commit is on that tip and the witness is that commit or
  an ancestor of it — containment, not equality, so a `--no-ff` landing stamps from the run worktree
  and an earlier landing's marker does not. Under `in-place` it writes nothing to the tree: `LANDED`
  is DERIVED from the advertised tip (`UNATTENDED-STOPS.md` §12), and the verb prints that derivation
  or refuses, numbered. It does
  not refuse the default branch: the mandated lander refuses every other one, so landing happens
  exactly where that guard would otherwise fire. It READS THE REAP BACK: the newest line of the
  stop-guard's sidecar carries the harness listing of the cron store, and the verb compares the
  recorded keepalive id with it before the anchor round-trip. Two refusals — the line is post-close
  and still names the id (reap it, end the turn so the listing is recorded again, re-run), or the
  newest line predates the close, so the check could run and has not (end the turn once; the
  stop-guard blocks a finished-and-unstamped stop and continues you). A post-close line without the
  id prints `keepalive-reaped: checked`; no sidecar, or no recorded id, prints `unchecked` with the
  reason and lands. It parses nothing beyond a substring test for the id, and it does not check that
  the id was ever this run's job. Where `RUN_CLAIMS` is `on` it writes `landed` into the run's claim
  once the record is staged; a claim it may not write is announced on one line and never fails it.
- `--rescope` — records an AMENDMENT to the build's own scope: `--act retire|supersede|add|defer`, the
  unit as `--item`, an optional `--successor`, and a reason. M3 delegates that scope and M2 names the
  first three acts; this verb is the record. `defer` sets a roster unit aside against an open ask so
  `build-complete` can carry it forward (`UNATTENDED-STOPS.md` §15); it refuses `--successor`, and like
  `retire` and `supersede` it is owed to the owner at the wrap-up. It RECORDS rather than acts: a row derived from the change it just
  made is a summary, and a check comparing the two confirms the driver instead of
  checking it. Nothing forces the call to precede the edit, so the row is a declaration in shape
  rather than in enforced ordering: the pair catches an amendment made with NO record, never a
  truthful-looking row attached to a different edit.
- `--dispatch` — records the WRITE-SET DECLARATION a concurrent dispatch owes: `--pass <unit-id>`
  and a REPEATABLE `--writes <path>`, one path per occurrence. The build method requires two path
  lists written down before two passes run together, and until this verb nothing read one. It decides
  two of that condition's three clauses — the intersection test, and the shared-record refusal in
  BOTH halves, so a generated index alone is accepted and only the index TOGETHER WITH its generator
  is refused. The third clause is a judgement about meaning and is refused as undecidable rather than
  faked. A DECLARATION IS APPEND-ONLY: every call parks its own row at the current
  anchor and nothing rewrites, supersedes or retracts an earlier one, so a re-declaration of the same
  unit is ACCEPTED whatever its relation to the row before it — wider, NARROWER, or disjoint. A pass
  that discovers it needs fewer paths than it declared says so, and both rows stand. M6 sanctions
  several pass kinds per unit, and a later row is read the same way whichever it is. What the verb
  REFUSES is overlap with a SIBLING pass still open, the disjointness question it exists for and the
  one thing here that is unchanged; a unit's own rows are never siblings of each other. A pass's
  COMMIT is the one whose `Pass: <unit-id>` trailer names it; a commit with no trailer falls back to
  its subject, and `Pass: none` names no unit. Before any of that it runs the DECLARED spec-token checker, `SPEC_TOKENS_CLI`, over the
  live tree and refuses the dispatch when it exits non-zero: the checker's bar join grades LIVE specs,
  an unattended build closes each unit spec in its own build commit, and this verb is the one point
  that sees a spec before its unit builds. A blank or absent key is an ANNOUNCED skip on stdout,
  never a silent pass. Where `RUN_CLAIMS` is `on` it reads the run's claim as the holder after every
  local refusal and before the row: another session's claim is check 108 and no row is written.
- `--review` — records ONE review round for a subject and reports what the loop is doing:
  `CONVERGING`, `CONVERGED`, `NON-CONVERGENT`, `CEILING` or `BOUNDED`. The round is an append-only
  `review` line in the parked region, a `history` kind, so it never inflates the count of decisions
  the owner must be shown. A round re-arms the loop only if its confirmed-blocker count is STRICTLY
  smaller than the round before — and a subject that is NOT the build slug, a spec audit, takes at
  most the declared `REVIEW_ROUNDS` rounds (kit default 1) before it exits `BOUNDED`; the build slug
  is the closing diff review and its bound is the runaway ceiling, so it converges or backstops as it
  always did. At a TERMINAL exit — `CONVERGED`, `NON-CONVERGENT`, `CEILING` or `BOUNDED` — on EVERY
  subject, spec subjects included, the round REQUIRES `--highs <n>` and `--minors <n>`, the confirmed
  HIGH and MEDIUM-plus-LOW findings standing at the exit, and writes them before the disposition:
  `blockers <b> · <EXIT> · highs <h> · minors <m>[ · disposition promote]`. Owner rulings of
  2026-10-04 for the closing diff review, the build-slug subject, and of 2026-10-05 for a spec
  subject: every finding a terminal exit confirms is promoted, one unit per BLOCKER and HIGH and the
  MEDIUMs and LOWs batched into one unit, two only across disjoint write sets. So `promote` is the
  ONLY value a terminal exit can record. It is REQUIRED whenever anything stood, "because every
  confirmed finding there is promoted", and refused when nothing did, since it "promotes nothing, and
  the gate would read the row as owing a unit". `fold` is refused at every terminal exit of every
  subject, which "folds nothing: every confirmed finding is promoted, the MEDIUMs and LOWs batched
  into one unit or two". `fold` survives only as the reading of a row written before spec subjects
  counted their exits, which carries no counts. A record naming no value where one is owed leaves the
  gate inferring one from ids. It refuses a verdict or a disposition outside its closed set, a
  missing subject or count, a terminal exit missing either count or a disposition it owes, `fold` at
  a terminal exit, a disposition or either count on a round that is not a terminal exit, and a round
  on a subject whose loop has already ended. Check 2 reads a row carrying both counts as owing
  `blockers + highs`, plus one for the minors when any stood, new non-WONTDO unit ids; every other
  row keeps the floor of one.
- `--check-commit` — `--check-commit <message file>`, run by the `commit-msg` hook on EVERY commit.
  It binds the run whose branch this worktree has checked out and is silent when there is none. A
  `Pass: <unit-id>` trailer must name an open dispatched pass, and the staged paths, less the
  run-state file, the unit's brief rows, the generated outputs and gen-region-only changes, must sit
  inside that pass's declarations; otherwise it refuses, naming each path and printing the
  `--dispatch` that widens the declaration while widening is still legal. No trailer on a subject
  naming an open pass is refused too, asking for `Pass: <unit-id>` or `Pass: none`. It writes
  nothing; a `--no-verify` commit skips it, and check 23 still grades that pass at the close. An
  AMEND of a pass commit is graded too, but an undeclared path in it is refused with no widening:
  a `--dispatch` would anchor at the commit the amend replaces, which check 23 never grades.
- `--claims` — every run claim on the remote, one TAB-separated row each: slug, node, status,
  beat age in seconds and verdict, `live`, `stale`, `held`, `terminal` or `unknown`, sorted by slug;
  `claims: none` when there is none, and exit 2 with check 109 when the remote does not answer, never
  an empty list. Where `RUN_CLAIMS` is not `on` it prints the single line `claims: off`, exits 0
  and reads nothing, since no verb writes or reads a claim then; `git ls-remote <remote>
  'refs/gov/runs/*'` still shows a leftover one. It takes no slug and decides nothing about who
  drives: `UNATTENDED-STOPS.md` §7 is what the verdicts mean.
- `--beat` — `--beat <slug>`, the resume tick's heartbeat for a run `--liveness` reads `LIVE` on this
  host: it renews that run's own claim when due and prints exactly one `beat —` line, `renewed` or
  `skipped: <why>`. It writes only a claim that is absent or the run's own, and refuses nothing but a
  missing record; `RUN_CLAIMS` off is a skip naming the switch.
- `--version` — prints the kit's own version and exits, touching no record. It is here because it is
  DECLARED, and a declared verb nobody documents is one nobody uses to answer the question this kit
  cannot answer for them: which build of it they are talking to. It takes no slug and no run, so it
  is the one verb safe to call before a run exists.

- `--hold` — the non-terminal stop. `--hold <slug> --code <c> --until <cond> --reason <text>`
  plus exactly one of `--reaped <id>` and `--keepalive-unreachable <node>`. It writes `HELD`, the
  code, the release condition, the phase it was held from and the moment, and RELEASES the slug's
  lease; `--resume` is the only way out. The code comes from a SECOND closed vocabulary beside the
  halt codes, never an extension of them — a halt code ends a run and a hold code pauses one, and
  one list would let a pause be recorded as an ending. Every refusal is numbered and comes before
  any write: an already-HELD record, a dirty tree, an unpublished tip under `ANCHOR_SCOPE=published`,
  a code or condition outside its grammar, a keepalive neither reaped nor recorded unreachable,
  because a job still firing into a held run re-dispatches its units at the next tick, and a
  process the slug's driver recorded still alive once its orphans are reaped. One
  exception to the published-tip clause: under `--code platform-unavailable`, and only when the
  remote does not ANSWER, it accepts the unpublished tip and records it as `hold-unpushed`. In the
  SAME write it decides whether a DURABLE restart is owed and records `resume-owed` and
  `hold-streak`, printing the schedule name, its fire instant and the prompt for the agent to file.
  An optional `--pending-run <runId>` names the Workflow run of a review that deferred twice; it is
  recorded as `hold-run`, rewritten EMPTY by a hold without it, printed on the HELD checkpoint and
  named by a take-over's relaunch line, and a value outside 1 to 64 letters, digits, `_` and `-` is
  refused with the rest. Where `RUN_CLAIMS` is `on` it writes `held` into the run's claim once the
  record is staged, announcing on one line a claim it may not write. The contract is
  `UNATTENDED-STOPS.md`.
- `--handoff` — the exit for a run whose work is sound and which an owner must land, or decide
  first. `--handoff <slug> --code owner-landing|owner-decision --reason <text>` plus exactly one of
  `--reaped <id>` and `--keepalive-unreachable <node>`. It is `--hold` with the condition fixed at
  `owner`, so every refusal a hold makes applies and no durable restart is owed, and it is the only
  producer of the two hand-off codes, which `--hold` refuses. It adds the landing recipe as a
  `handoff` row the owner is shown, and `units-at-landing` and `asks-at-landing` as `--close` writes
  them. `owner-landing` is refused over a bar that is not GREEN unless every red leg reads INHERITED;
  `owner-decision` requires a parked decision row. The contract is `UNATTENDED-STOPS.md` §2 and §4.
  The recipe's last command is `--settle`, through this kit's own repo-relative path. After its
  last refusal it makes `--park`'s refresh and records `refreshed-at` with its writes.
- `--settle` — writes what git proves onto a slug's live record. `--settle <slug>`. A hand-off its
  owner landed, which every deriving reader already reads `LANDED (attended)`, becomes `phase:
  LANDED` with `landed-by: attended` and `landed-derived`. An `ABORTED` record first committed before
  `HANDOFF_CUTOFF`, and a working record whose `--liveness` verdict is `STALE` or `UNBOUND`, gain
  `work-landed-at: <witness> <tip>` when the content predicate reads the run's own commits on the
  advertised tip and none reverted; the working one gains `abandoned` too and keeps its phase. It
  refuses, numbered and before any write, everything else, an unanswered remote and an undecidable
  predicate; a settled record is said so and not rewritten, and the re-run retries the run claim's
  status write over a claim of the record's own lease still `held` or `live`, so a first write that
  did not complete names this re-run as its remedy. It STAGES and never commits. The contract is
  `UNATTENDED-STOPS.md` §12.
- `--abort` — the sole producer of `ABORTED`. It requires a recorded reason, a HALT CODE from the
  effective vocabulary, and both agent-attested items, and no machine item: an aborted run landed
  nothing, so the machine items assert obligations it does not have, while the idle-wake is still
  orphaned and the parked decisions still unseen. The code is validated before it is recorded and the
  refusal names the legal set; it is the twelfth authored fact, and it exists because one terminal
  phase said a run stopped and never said why. From `HANDOFF_CUTOFF` an `ABORTED` record means
  DISCARD, and an abort naming a hand-off-shaped halt code, on a record first
  committed on or after it prints a notice naming `--handoff`, then aborts as asked; it never refuses.
  With both attested items met it makes `--park`'s refresh and records `refreshed-at` beside the phase.
  Where `RUN_CLAIMS` is `on` it writes `aborted` into the run's claim once the record is staged;
  a claim another session holds is announced and the abort still lands, which is how a run
  that lost its claim ends: `--abort <slug> --code claim-lost`.
