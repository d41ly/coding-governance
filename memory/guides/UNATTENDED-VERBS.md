<!-- gov:kit unattended@1.90 -->
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

## The paths, in order

The unattended Skill is a ROUTER into this section: it picks the path and carries the commands a
render fills in, and this section carries each path's steps in their order, the condition that
selects each one and the section of the contract it answers to. This file is copied and never
rendered, so where the Skill shows a value only the render can give, this section names the
`.unattended.conf` key that supplies it: the scheduler calls are `KEEPALIVE_CREATE`,
`KEEPALIVE_DELETE`, `RESUME_SCHEDULE_CREATE` and `RESUME_SCHEDULE_DELETE`, the lander is `LANDER`,
the prompt token is `AUTH_PARAM`, the anchor is `ANCHOR_SCOPE`, and `unattended.sh` is the kit's
driver at the path the Skill renders. "The build method" is the memory tree's build-method guide,
and `M<n>` is a section of it. The Skill keeps four blocks a gate reads there: the directive table
with its scope rule, the two items with no override, the process-ledger rule, and the hold routing
under its Close heading.

### Before any path — the idle-wake

1. **The run's first act, before ORIENTING, not merely before preflight:** schedule the idle-wake
   with `KEEPALIVE_CREATE` at the `KEEPALIVE_INTERVAL` cadence and keep the id, because `--preflight`
   refuses without it. It sits above every path because the prompt and playbook paths orient,
   research, choose, write a build folder and push BEFORE their first verb, which is the longest
   unattended stretch a run has; a step written inside one path is a step the others do not run.
   `Resume` is the one path it does not bind: a resumed session inherits a job it did not schedule,
   so that path reaps before it schedules.
2. **What the tick runs: TWO acts, in order**, and only once this session's `--preflight` has written
   the run's record; before that it does nothing. A tick issued earlier meets a refusal that is
   expected and is never a signal to reap the keepalive `--preflight` is about to need: `--resume`
   refuses with check 10 when no run-state file exists, with check 26 on a re-run build whose
   previous record is terminal, or with check 58 naming another branch where this worktree's copy is
   a HELD or working record carrying a lease and this worktree is not on its run branch; under
   `in-place`, where a landed record stays LANDING until the next `--preflight` retires it, `--resume`
   prints nothing to resume and `--audit` then refuses with check 51.
   - FIRST, `unattended.sh --resume <slug> --keepalive-id <your own id>`. For the holder it writes
     nothing to the record, because liveness is derived from what `--liveness` reads and this tick
     moves it; where `RUN_CLAIMS` is `on` it reads the run's claim on the remote and renews it when
     due, and a claim another session holds refuses it at check 108, which you end with
     `--abort <slug> --code claim-lost`. The act refuses a session that no longer holds the slug
     before the second act runs.
   - SECOND, and only when the first neither refuses nor prints `still held`,
     `unattended.sh --audit <slug>`. After either of those outcomes this session does not drive the
     slug: acting on a `STALLED` verdict would re-dispatch units a live holder is driving, or a held
     run's units — the double drive the lease exists to stop.
   - A unit line reading `PROGRESSING`: do nothing. `STALLED`: stop the unit's task, record why with
     `--park` or a brief note, then re-dispatch that unit with a brief naming the stalled command and
     that it is skipped. Its figures are the tree's; whether a process is stuck is the
     process-monitor kit's question.
   - A registered task's `STALLED` line: read its heartbeat file first, stop the task — an `Agent` by
     its task id, a process tree through the process-monitor kit's reap, the `PROCMON_CMD` the
     project declares, because a stopped background shell can leave its detached children running —
     record why with `--park` or a `Decided:` line, run `--release-task <slug> --task <name>`, then
     re-run it bounded or leave it parked.
   - Whoever STARTS a background task registers it first with
     `--register-task <slug> --task <name> --heartbeat <absolute path>`, and releases it when it ends.
   - On `STALLED` act, and never end the turn by asking: the owner is absent, and a session bound to a
     non-terminal run has a stop-guard that refuses the stop. The probe is the run's heartbeat too:
     `--audit` is journaled like every verb but `--version` and `--plan` (protocol §2), so a stalled
     run reads as a gap in that journal rather than as silence.
3. **If the run never starts, reap it anyway.** Every path can refuse, and a job left by a run that
   never began is orphaned exactly like one left by a run that ended, with no run-state file for a
   later reader to find it through. `KEEPALIVE_DELETE` before you stop.

**What wakes a stalled run** is protocol §5's three actors, and all three read one predicate,
`unattended.sh --liveness <slug>`, the one to run by hand to see what they will see. The stop-guard
refuses a turn end while the run is non-terminal and not HELD, up to `STOP_GUARD_BLOCKS` times; the
stall-recorder writes an API-error end to the `stall` sidecar; the resume-tick resumes a run from
another process on the verdicts §5 names as acting, not `STALE` alone. The tick's registration line
is in the kit README.

### Which path — the opening fence

Before any verb, a value mixing a slug and ids, or a prompt naming both, is refused: say so, print
the two legal forms — `/unattended <slug>` and the scaffold route — reap the keepalive, and stop. A
run cannot extend a committed mandate, so a mixed value has no honest reading. A topic with no
playbook is the AUTHORING path, never the playbook-run path: preflight refuses a `playbook:` that
does not resolve at BASE, so a no-playbook start never reaches it. Making a playbook and following
one are two acts with two authorizations.

### Start a run — `slug`

0. **Read the build method WHOLE, before anything else.** Not conditionally: every directive in the
   Skill's table points at a section of it, so a run that has not read it is bound by a set that
   resolves to nothing, and `--preflight` refuses a tree where it is absent. Two rows carry a
   consequence before you waive them. **`reuse-first`**: the `reuse-probed` item reports the waiver
   and its recorded reason at `--close`, and where the project sets a reuse-evidence cutoff the memory
   gate refuses a spec whose §10 lacks EITHER the recall terms or a probe result; a waived run's spec
   §10 still NAMES the waiver, which the gate accepts as a finding. **`land-once-done`**: the
   Definition-of-Done item that observes completeness stays, and still owes an override at close
   unless every unfinished unit is carried forward (`UNATTENDED-STOPS.md` §15).
   Neither `recipe` row states its rule, deliberately: following a declared procedure to the letter
   IS the pass loop and its regrounding rule (M7), and recording what was produced IS the wrap-up
   derivation (M9).
1. **The build folder IS the authorization, at the anchor `ANCHOR_SCOPE` declares** (protocol §1,
   which states what each anchor costs; the run-state file records which one was used). On the
   **default-branch** anchor the folder was committed before your branch existed, and preflight
   REFUSES a folder you created. Under **published**, the tip the remote advertises for your OWN
   branch also counts, but only where the folder declares `authorized-by: prompt` or `recipe`; a
   `slug` folder, which is what no `authorized-by:` key means, is refused there. Under **local**, a
   folder committed anywhere in HEAD's history counts, in every mode `slug` included, with no push.
   You do not create the run-state file; preflight does.
   - **Not on the default branch? PUSH YOUR BRANCH FIRST** under `published`: an unpushed commit
     authorizes nothing, and the refusal names the branch the remote does not advertise. Under
     `local`, COMMIT and do not push: the run may start from the worktree branch, or the local
     default branch, that wrote the folder. Under any other value only the default-branch anchor
     counts, and the build has to be landed first.
   - **A build already run once is not closed to you.** A `RUN.md` in a terminal phase is RETIRED by
     preflight to `RUN.<phase>.<blob8>.md` beside it, and a fresh one starts; stdout names both paths.
     Never move, edit or delete a finished record yourself.
   - **READ the README — it is also the ROSTER.** Its authored Units table is the build's roster
     (M2), and its Start-here section carries the state, the classification and the next action.
2. **Only if the invocation named a directive to waive: THIS IS THE LAST OWNER TURN.** Otherwise skip
   it. Ask ONCE, one `AskUserQuestion` covering every named handle, in groups of four at most, the
   call's own limit. **DEFAULT-DENY**: a handle named but not confirmed WITH A REASON is not waived —
   the flag requests the question, the answer grants the waiver. Carry each confirmed pair into step
   3 as `--waive <handle> --reason "<text>"`, and say what the waiver costs for the two handles step 0
   names. From the next command on nobody can answer: `--waive` is accepted by `--preflight` alone,
   and only while no run-state file exists or the set matches the recorded one, so a re-preflight
   after a compaction re-issues the recorded set.
3. **Preflight**, handing over the idle-wake id and any confirmed pairs:
   `unattended.sh --preflight <slug> --keepalive-id <id> [--waive <handle> --reason "<why>"]`. Its
   refusals are its verb entry's, each names itself, and it writes nothing until all pass. It does
   NOT refuse because another build is live: it announces the concurrent runs and continues. One line
   before `preflight OK` states the spec-audit posture —
   `unattended: spec-audit — opted in by README spec-audit: <date>`;
   `unattended: spec-audit — opted in by project default SPEC_AUDIT_DEFAULT: <date>` when the README
   declares no key (`TOOL-aBlindedTrial-7`; the README key wins whatever it says); or
   `unattended: spec-audit — not owed (opt-in)`. The audit is OPT-IN per build (owner ruling of
   2026-09-20, `TOOL-aBlindedTrial-6`); the README key is read at BASE and the project default at
   the default-branch side of it, so a working-copy edit opts nothing in or out, and a value that is
   not a date is a refusal. **The opt-in is the OWNER's, never yours** (`TOOL-aWardedAudit-4`): do
   not write `spec-audit:` into a README you author, which preflight refuses under `authorized-by:
   prompt` or `recipe` (check 89), except a `prompt` README whose prompt record at BASE quotes the
   owner asking for the audit (owner, 2026-10-05). `not owed` names the owner's cue, two or more
   units or a FORKED spec: carry it to the wrap-up and decide nothing. Keep the line: the harness
   call needs it, and after a compaction `--status` carries it as `· spec-audit <date>`.
4. **`/session-kickoff`, if the project ships it — after preflight, never before.** Its unattended
   hand-back fires only when a non-terminal run-state file exists, which only `--preflight` creates;
   invoked first it halts at its READY card for a confirmation nobody is present to give. It buys the
   manifest audit, the pointer map, the tier rule and the front-loaded traps. Skip it silently where
   the project has no such skill.
5. **If the README carries `asks:`, read `UNATTENDED-ASKS.md` whole before the first roster row.**
   Orient per mandated ask, ending each in one state (§3); park an ask graded not ready as an owner
   call, never a guess (§4); file a discovery in this build's own `BACKLOG.md` with its `SEV` row in
   the same commit (§5); touch a dead path in another build's ask only under the repoint rule (§7).
   Authority is protocol §1's `may:` rule, and nothing an ask carries adds to it. The build's first
   spec commit deletes a scaffolded README's `status: OPEN` (§1).
6. **A pre-flip BASE is parked, never relocated.** When preflight's notice says `BACKLOG_MODE`
   differs between the anchor and `HEAD`, or the branch forked before the tree switched to per-build
   backlogs, park with the recipe the memory-tree kit's `migrate_backlog.py --recipe` prints. Never
   run `--relocate`: a relocation is the owner's merge.

### Ids go through the scaffold

A run may not write the folder that authorizes it, so an id list reaches a build only through a
README the OWNER lands (`UNATTENDED-ASKS.md` §1).

1. `unattended.sh --preflight "<the value>" --keepalive-id <id>` — the ids, the ids a prompt names,
   or a filing home's slug, quoted as one argument. It refuses by design and writes nothing, printing
   the scaffold recipe with your tokens, or for a filing home the recipe beside that folder's asks.
2. **Relay the recipe to the owner verbatim.** Do not run it: the scaffold stages a README the OWNER
   commits and lands, which is what makes it an authorization.
3. **Reap the keepalive and stop.** The next run is `/unattended <slug>` on the landed folder.

### Start a run from a PROMPT — `prompt`

**Only when the invocation carries `AUTH_PARAM`.** The token IS the authorization gesture; inferring
it from wording would let a description of a build start one. No token, no prompt path. The fence
binds a playbook-authoring start exactly as it binds a code one.

**The value is everything after the token to the end of the line**, one layer of surrounding quotes
stripped, and it is a path to a prompt file or the prompt itself. Test for the FILE FIRST; a
relative path resolves against the repository root, never the session's own directory.

| The value | What it is | What you do |
|---|---|---|
| no whitespace, names a readable file | a path | read it; the FILE'S CONTENT is the prompt |
| no whitespace, names nothing readable | a refusal | say the path did not resolve, and stop |
| has whitespace, names nothing readable | the prompt itself | take it verbatim |
| has whitespace AND names a readable file | a refusal | say the value is ambiguous, and stop |

The file test runs first because a quoted path containing a space arrives as one argument with
whitespace in it; reading that as a prompt would silently make a file the whole scope of the build.

- **A prompt that NAMES IDS is not this path**: take the scaffold route with those ids and write
  nothing, since a run that wrote its own ask mandate would be authorizing itself.
- **This path needs `ANCHOR_SCOPE` to be `published` or `local`.** Under `default-branch` no folder
  you author can resolve, so say so and stop, writing no build folder nothing can authorize.
- **`authorized-by: prompt` in step 3 is not bookkeeping.** Omitted, the folder reads as `slug`, which
  this anchor refuses, and the refusal arrives AFTER the push with no owner turn left.

The steps are ORDERED: everything before the push is provably older than the commit that authorizes
the run, which makes "the owner was asked at the start" a property of the commit graph.

1. **Orient from the prose**, in the kickoff engine's manner, its steps 0 to 4: derive every field you
   can from the prose, the memory tree and the code, and do not ask yet. **RUN the orientation
   probes here, before step 3 writes the roster** — the engine's step 4 names which; a seam or prior
   record found after the roster is pushed costs a commit and a push to re-decide.
2. **Decide whether to ask, ONCE.** The field set is the kickoff checker's,
   `bash <check-script> --task-skeleton`. ACCEPTANCE and GATES are disqualifying; any other gap is
   askable once. **The only owner turn there is**: one `AskUserQuestion`, every gap in it, four
   options at most per call. If ACCEPTANCE or GATES is still missing after it, stop without writing
   anything: no run started, so `--abort` and `--park` refuse with no run-state file, and protocol
   §13 exit 5 does not reach here.
3. **Write the build folder**, `builds/<slug>/README.md` under the memory root, with ALL SIX required
   front-matter keys — `slug`, `node`, `opened`, `streams`, `roster`, `ids` — plus
   `authorized-by: prompt`, and the generated-region marker pair `gen:build-index` with its close, or
   preflight refuses at step 5 that *the build README's generated markers are malformed*. **No
   `spec-audit:` key**: under this mode check 89 refuses it, because a run may not opt itself into
   the audit.
   **The prompt goes to a RECORD, never into the README**: under `builds/<slug>/prompts/`, carrying
   its `**Serves:**` line and, where the value was a path, the path it came from — the bytes travel,
   because the authorization may not point at a file editable after the run starts. Not the README:
   its heading canon is closed and its slots carry byte ceilings; its marker matcher reads column 1
   blind to fencing, so a prompt quoting the marker plants a second one; and a malformed record reds
   the memory gate here, where you can still fix it. The README states the build in its own words
   and points at the record; clarifications ride the record. The roster may be provisional.
4. **Commit, then PUSH THE BRANCH**, in that order, under `published`. Skip the push and preflight
   refuses with `the remote advertises no tip for the branch this run is on, so nothing published
   authorizes it`. Under `local` the commit is enough and no push is owed.
5. **Preflight**, as on the slug path; it records the mode from the file you pushed.
6. **The kickoff hand-back**, at the slug path's step 4 and for its reason.

**After any later roster change, commit AND, under `published`, PUSH before the next authorization read**: a roster
grown and committed but not pushed blocks `--close` on `authorization-reachable`, which has no
override. `researched` and `solution-tested` are scoped `all`, and M12 decides when a build owes them.

### Start a PLAYBOOK run — `recipe`

A playbook exists and the owner wants N pieces from it; the run FOLLOWS it to the letter. `recipe`
turns on the playbook resolution at BASE, the two piece-scoped Definition-of-Done items and the two
`recipe`-scoped directives. **The mode is for DECLARED CONTENT** — pieces landing where the playbook's
`outputs` globs say — and an ordinary code build takes the slug or the prompt path; the refusal that
was to enforce this was withdrawn unbuilt, so it is prose you keep, on both entry points.

0. **Read the build method WHOLE, and the playbook whole**, then the playbook again per piece: it is
   segmented for that. Writing the build folder yourself needs `published`, for the prompt path's
   reason; where the owner landed the folder first, either anchor works and step 4's push is skipped.
1. **Orient from the playbook**: what one piece IS, where pieces land, which checks run over one and
   which over all N. What it leaves open is usually the COUNT, and which location when its `outputs`
   globs admit more than one.
2. **Decide whether to ask, ONCE**, as on the prompt path; from step 4 on nobody can answer. The field
   set is narrower, so the ordinary case is no question at all.
3. **Write the build folder** with the six required keys and the marker pair, plus
   `authorized-by: recipe`; `playbook: <repo-relative path>`, resolved at the pinned BASE and not at
   HEAD, since a playbook this run wrote is not one anything older can vouch for; and `pieces: <n>`,
   the count the close is measured against, where absent, non-numeric or zero is a refusal.
4. **Commit, then PUSH THE BRANCH**, in that order, where you authored the folder.
5. **Preflight.** It resolves the playbook at BASE and refuses one declaring no output globs, no piece
   grain or no declaration block — fix those in the playbook and land it, never in the working tree.
6. **The kickoff hand-back**, at the slug path's step 4.

**Record each piece as it is made**, with `--record-piece` per piece and `--record-set` once over all
N: the two piece-scoped items read the records, never the transcript. A piece record is hash-joined
to its piece, so editing a piece after recording makes the record STALE. The set's identity is the
ordered list of this run's piece hashes, DERIVED, since a caller naming its own set could name one it
did not produce. **Never edit the playbook you follow**: propose with `--propose`, joined to the step
that provoked it, and the amendment is a separate authoring run.

### Author a PLAYBOOK — `prompt`

A run that MAKES a playbook takes the PROMPT path, never `recipe`: it has no playbook to name, and
its diff lands outside any declared output glob. Research the subject and the code the pieces relate
to, decide what one piece IS, then write the playbook from the memory tree's `PLAYBOOK-TEMPLATE.md`,
whose canon is closed; the build method's M12 binds the research and the test. Validate with the
kit's `check-playbook.sh`, which grades every tracked file carrying a declaration block, so a
playbook that does not validate cannot land.

**The playbook must be older than the BASE of the run that follows it.** Whenever the following
run's build folder was committed before that run, preflight refuses a playbook the run committed
itself, under either anchor, with *a recipe-mode build README names a playbook that does not resolve
at the pinned BASE*. The one unprotected state is a run authoring BOTH its build folder and its
playbook under `published`: nothing refuses it, so **land the playbook in its own earlier run, then
start the run that follows it.**

**Amendment rides this path.** Proposals accumulate on the run-state files of the runs that found
them; an owner-instructed run reads them, edits the playbook and lands it. CHECK, not a gate: cite
the proposals acted on, and say which were declined and why.

### Produce pieces ATTENDED — not a run

An owner is in the loop: no authorization, run-state file, phase, idle-wake or Definition of Done.
The merge bar still sees what was PRODUCED: the per-piece and set records are tracked files the
playbook leg reads without knowing who wrote them. That leg CLASSIFIES and reports; what BLOCKS on
its counts is `--close`, which this path never calls, so on this path they are evidence a human
reads, and only a record shape the leg refuses reds the bar. Both writers take a records ROOT instead
of a slug — `--record-piece - --records-root <root> ... --run <label>` and `--record-set -
--records-root <root> ... --run <label> --set <hash,hash>` — the root being the playbook's own
`records` declaration. `--set` is a CLAIM here rather than a derivation: take the hashes from the
piece records just written, not from memory. The code-build CHECK binds here with no machine half at
all, and the kickoff engine's exit list has no entry for this path, deliberately.

### While it runs

- **No merge bar and no self-test suite inside a pass**, yours or a dispatched agent's (M6). A pass
  verifies with the direct check its spec names; a unit needing a suite verdict returns the need.
  The bar runs ONCE at `VERIFYING`, after the last unit is terminal: `--close` runs the plain bar for
  `gates-green`, and kit work owes the flagged form the Close steps spell. Where a pass touched files a leg
  guards and you judge a bar necessary, the plain bar with no flag is the scoped form, at the main
  loop. gate-guard.js refuses a `GATE_FULL=`/`GATE_SELFTESTS=` prefix, a self-test runner or any
  `*.test.sh` on the run branch until the record reaches `VERIFYING`, sidechain agents included. The
  move into `VERIFYING` announces, under every `LANDER_MODE`, when the run's range touches a path
  `SELFTESTS_OWED_PATHS` declares; the driver sets `GATE_SELFTESTS` nowhere.
- **The process ledger** is the Skill's rule: the driver records every command it starts and reaps
  only those, once their driver is gone, and `--status` prints `orphans <n>` while any wait.
- **Keep the phase honest**, and give every phase claim a WITNESS — a sha, a tag, a run id. A claim
  with no witness is skipped by the oracle that would judge it. Move it as each pass ends with
  `--phase <slug> <PHASE> --witness <sha>`; the members are named for the build method's pass kinds.
- **Park what you refuse to decide** with `--park <slug> --item "<question>" --reason "<options seen,
  and why you refused>"`, the only route a gate reads. Re-running with the same question and reason
  is a no-op; it is refused on a finished record, where `--abort` is the verb.
- **A STRICTLY BENEFICIAL discovery is ADOPTED, never parked** (protocol §11): one that makes an
  observable this repo already MEASURES strictly better, makes nothing it measures worse, and
  survives M3's vetoes joins this build now through `--rescope --act add`. One failing the first two
  clauses is an ask filed in this build; one tripping a veto is a park. A BLOCKER between you and
  your own landing is a discovery.
- **A playbook you FOLLOW is not one you may edit**: `--propose <slug> --item "<amendment>" --step
  "<step>" --reason "<what provoked it>"`. Nothing blocks on a proposal, `--status` counts them
  apart, and one amendment against two steps is two rows.
- **Record what each build pass was handed**: write the brief as a tracked file under the build's
  `prompts/`, then `--brief <slug> --unit <unit-id> --path <file>`. A `history` kind; an unchanged
  re-brief is a no-op and `--status` grades the LATEST row per unit.
- **Record a verdict where a check ran over content**: `--record-piece` per piece and `--record-set`
  once over the set, with `--verdict PASS`, `FAIL`, or `NA` for a leg whose declared coverage mode
  is dark. The verdict is validated for SPELLING alone — nothing compares the word to an outcome.
- **When building uncovers what speccing could not, AMEND — do not stall** (M2, M3):
  `--rescope <slug> --act retire|supersede|add|defer --item <unit-id> [--successor <unit-id>]
  --reason "<what building uncovered>"`; `defer` is the close's carry-forward act, below. The
  README's GOAL statement may not be amended and a governance carrier's stated constraints are out
  of reach. An id in the units region never LEAVES it: retiring is a status flip to `WONTDO` with a
  successor or reason, because the authorization compares BASE against HEAD as a subset. `retire`,
  `supersede` and `defer` are surfaced-class rows your `parked-decisions-surfaced` attestation must
  cover; `add` stays history.
- **Before dispatching a pass, DECLARE its write set** (M6): `--dispatch <slug> --pass <unit-id>
  --writes <path> --writes <path>`, one path per `--writes`. It refuses two passes claiming one file
  and a pass claiming a shared mutable record; a generated index alone is fine and only the index
  WITH its generator is refused. Whether a file is a contract the sibling reads is a judgement no verb
  makes. A pass needing another file declares again BEFORE the commit, naming only the paths it
  adds: every row at one anchor stands and the pass may write their union, which `--dispatch` prints
  as `dispatch effective`. A narrower row is accepted and frees nothing, and a row at a LATER anchor
  is a new pass, graded on its own. **End the pass commit's message with a `Pass: <unit-id>` trailer**,
  and a commit naming a unit but no pass with `Pass: none`. Where the `commit-msg` hook runs
  `--check-commit`, a pass commit staging an undeclared path is refused with the `--dispatch` that
  widens it: run it, then commit again.
- **Drive the build as ONE program** (M6 `passes-harnessed`, protocol §12): the build harness runs
  SPEC, then — only where the build or its project declares the audit — AUDIT and DISPOSAL, and hands
  back the ordered roster on a terminal `--review` verdict, or at SPEC completion when the audit is
  off. Pass `specAudit: <date>` when the preflight line read `opted in by README spec-audit: <date>`
  or `opted in by project default SPEC_AUDIT_DEFAULT: <date>`, and omit it on `not owed (opt-in)`;
  the fan-out hook compares the value with the run's pinned `spec-audit` fact and refuses any other.
  The unit harness then builds ONE unit per call from its brief and its spec. Every call is made by
  `scriptPath`, never by `name`: the fan-out guard's read-window narrowing is conditional on
  `scriptPath`. Read the build method WHOLE before the first call. The child runs no gate, suite or
  bar, verifies with the one check that exercises its change, and bounds every command, skipping and
  naming a non-code command that does not return in its bound. The call carries `scratch: <your
  session scratchpad, absolute>` and refuses without it; the child refuses too, without the key or
  with a `ground` that does not name it. **Every call also carries `base: <the run's pinned base
  fact>`**, audit on or off: it pins the spec audit's checklist and the spec commit's checklist at
  the base the run was authorized at, and the harness refuses a declared `specAudit` without it.
  - **A review the platform killed DEFERS**: on `exit: 'deferred-platform'` nothing was recorded or
    built and every returned agent's result is on disk, because the build harness runs its audit under
    `workerType: 'none'`. Re-run the harness ONCE with identical args;
    on a second `deferred-platform`, hold — `--code platform-limit --until "after <reset UTC>"` when
    the Workflow result names a usage or session limit, `--code platform-unavailable --until "probe
    api"` otherwise — each with `--pending-run <runId>`.
  - **Between dispatches re-read `--plan <slug> --paths`** and branch on every shape:
    `next: <id> (READY - build it)` dispatches; `(MISSING - spec it first)`, `(THIN)` and `(FORKED)`
    do NOT; `(UNDECIDED - plan a unit that closes it, or dispose it)` is oriented, never dispatched
    (`UNATTENDED-ASKS.md` §3); `next: none - every tracked spec is terminal` ends the loop;
    `next: none - no tracked spec grades as a unit` does NOT — halt and read the NOT A UNIT rows, the
    verb still exits 0. A child returning `committed:false` stops the loop. Nothing refuses the next
    dispatch for you: the one refusal of an early stop is `build-complete` at `--close`, and its
    escapes are a unit carried forward against an open ask or a recorded `--override build-complete`.
- **Run the bug-class checklist after every commit**, before the next pass: the memory-tree kit's
  `gotchas.py --for-diff HEAD~1..HEAD`. It takes a COMMITTED range, so before the commit it prints
  "touches no file", which reads like a clean checklist and is not one. Its stdout IS the checklist
  and it exits 0 whenever it prints one, and 1 with a `HYGIENE gotchas:` line when it refuses the
  range, so finish it rather than reading its status; a class already violated is the next pass. An adopter without that kit
  follows whatever its own build method names.
- **Check yourself** with `--status <slug>`, the units with `--audit <slug>` and what is left with
  `--plan <slug>`, which joins the README's roster against the tracked specs so a planned unit nobody
  specced reads MISSING. Out-of-session readers share `--liveness <slug>`. `--version` prints which
  build of the kit you are talking to. Where `RUN_CLAIMS` is `on`, `--claims` lists the claims on the
  remote, which is where a second node driving a slug shows up, and the resume tick renews a `LIVE`
  run's own claim with `--beat <slug>`, one `beat —` line.

### Review rounds, and the loop that ends itself

Record EVERY round: `--review <slug> --subject <id-or-slug> --verdict <verdict> --blockers <N>`.
`--subject` is the spec for a spec audit and the BUILD SLUG for the closing diff review; the verdict
is `CLEAN`, `CLEAN WITH FIXES` or `BLOCKED`; `--blockers` is THIS round's confirmed count. Act on the
state it answers (the rule is M4 and M8; the verb entry above states the recording):

- **CONVERGING** — strictly smaller than the round before. Fold and go again: on a SPEC subject the
  fold fixes what that round confirmed and only the exit promotes; on the closing diff review it
  fixes BLOCKERS only, and the rest carries to the exit (M8).
- **CONVERGED** — zero blockers; its confirmed highs, mediums and lows are still disposed by
  severity. The round records `--highs` and `--minors` on every subject, and `--disposition
  promote` whenever anything stood.
- **NON-CONVERGENT** — the count did not shrink. The loop STOPS and every CONFIRMED finding is
  DISPOSED BY SEVERITY: a BLOCKER or HIGH becomes a UNIT whose mechanism closes it, specced, audited
  as a SPEC, built and closed; a MEDIUM or LOW is PROMOTED too, on every subject, batched as the
  paragraph below states. Never folded, parked, waived, RETIRED or re-reviewed — a promoted unit
  flipped to `WONTDO` would satisfy both the promotion count and `build-complete` — and never
  DEFERRED to be carried forward, since `build-complete` carries only a unit the roster held when the
  run started. Record `--highs`, `--minors` and `--disposition promote`; `fold` is refused at every
  exit of every subject.
- **BOUNDED** — `REVIEW_ROUNDS` (kit default 1) reached on a subject that is not the build slug.
  Disposed exactly as `NON-CONVERGENT`, recorded with both counts and `promote`. A promotion here is
  not audited by the round that produced it: after `--rescope --act add` and the new spec, re-invoke
  the harness at round N+1 — a post-disposal re-invoke passes `auditIds` and no `subjectRound`, a
  fold re-invoke copies the `subjectRound` the CONVERGING return handed back, and `auditIds` and
  `subjects` are never passed together. Skip it and `specs-audited` refuses at `--close` where an audit is declared.
- **CEILING** — the runaway backstop fired: a defect in the predicate. Promote, land anyway, and
  record it in the build README.

**Every terminal exit promotes EVERY confirmed finding, and COUNTS them** (owner rulings of
2026-10-04 for the closing diff review and 2026-10-05 for a spec subject): a unit per BLOCKER and
HIGH, the MEDIUMs and LOWs batched into ONE unit, TWO only across disjoint write sets by M6. The
terminal round on every subject carries `--highs <H> --minors <M> --disposition promote`, refused on
a round that is not one. On a spec subject the build harness records them itself. Otherwise derive
both from the harness returns, never the report: on the closing diff review, per round, `<H>` adds
that round's `highs` and `<M>` adds `confirmed - blockers - highs`, summed over every round; on a
spec subject recorded by hand they are that exit round's `highs`, and its `confirmed - blockers -
highs` plus every UNVERIFIED finding the disposal promoted, with no summing, because a spec round's
fold fixes everything that round confirmed. Strictly smaller, never merely different: 2, 1, 2
changes forever. A subject whose loop ended takes no further round.

### Resume

Read the run-state file before anything else (`UNATTENDED-STOPS.md` §8 and §9 are the contract).

1. **`--status <slug>` first, because who you are decides the rest.** Your scheduler lists the
   record's `keepalive` job: you HOLD the lease — `--resume <slug> --keepalive-id <that id>`, reap
   nothing. You are the session the `session` fact names and the job is gone: schedule a new one and
   resume with its id. Otherwise you are TAKING OVER: reap the recorded job, read the result back,
   schedule a new one, then `--resume <slug> --keepalive-id <new id>`. If that resume REFUSES or
   prints `still held`, reap only the job you just scheduled, confirm from the listing it is gone and
   stop, removing nothing else. A check-58 refusal naming the run's branch means this worktree is not
   the run's: reap only your new job and resume from the worktree it names. Replace your OWN job only
   through `--resume <slug> --keepalive-id <new> --replaces <old>`.
2. **Woken by a durable scheduled task: `--scheduled <held-at>`**, the value its prompt carries. A
   refusal is the answer: reap the keepalive you scheduled, confirm it, leave the named task alone,
   stop.
3. **On the take-over branch, REAP the recorded id BEFORE you schedule a replacement.** The
   intuition that the job died with its process is MEASURED FALSE: both jobs of a run asserted dead
   were still firing in `KEEPALIVE_CREATE`'s own listing. Issue `KEEPALIVE_DELETE` against the
   recorded id, read the result back, and say what it returned. Then schedule the new one with the
   stall-probe prompt. Order: read, reap, schedule, resume, kick off, work.
4. **On the take-over branch, PUSH the record before any other work**: a schedule on another node
   compares the remote's tip with its own HEAD, and an unpushed take-over is the window in which two
   nodes drive one slug. Re-preflighting is never the remedy: it refuses a dirty tree and re-pins.
5. **Delete the durable restart only AFTER a take-over `--resume` whose record you pushed**:
   `RESUME_SCHEDULE_DELETE` against `unattended-resume-<slug in lower case>`, going on when no task
   has it. Never before that resume, nor on its refusal or `still held`.
6. **Then `/session-kickoff`, if the project ships it**, after a `--resume` that neither refused nor
   printed `still held`, before the first pass: a resumed session has no card, or a replay-written
   one, and its first commit would otherwise be a durable act nobody oriented.

### Close

1. **Move into `VERIFYING` first, under every `LANDER_MODE`, and commit the record the move stages**:
   `--phase <slug> VERIFYING --witness <sha>`. The move ANNOUNCES the owed flagged bar when the range
   from the pinned BASE touches a path `SELFTESTS_OWED_PATHS` declares; a resume or take-over finding
   the record at `VERIFYING` prints it again.
2. **Under `primary`, `--close <slug>` follows that commit.** Under `in-place`, `LANDER --prepare
   --slug <slug>` comes first, because the close's bar grades what HEAD carries; make NO second move
   after the prepare, since a move stages the record and that close refuses a non-empty porcelain.
   Between them run `--authorization <slug>`, which is not one: it stages and writes nothing, and
   grades the one non-overridable item the prepared merge can break before the close spends its bar.
   A refusal there ends the landing; take one of the two exits it prints. That close refuses BY NUMBER, with no `--override`, when HEAD carries no prepared merge or the tree
   is not clean including untracked files; it refuses a commit belonging to another build, then
   COMMITS its own record on top of the graded merge. Under `primary` the verb stages the record and
   names the commit you owe. A resume after the prepare reads a range holding what the merge brought
   in, so it may announce one flagged bar more than owed, never one fewer.
3. **When the `VERIFYING` notice named a surface, export `GATE_FULL=1 GATE_SELFTESTS=1` into that one
   `--close`**, under either mode. Its bar inherits both, and gate-guard.js admits the prefix from
   `VERIFYING` on. Under `in-place` the close adds `GATE_FULL=1` to its own bar; under `primary` it
   does not, and `GATE_SELFTESTS=1` alone leaves every guarded self-test leg the branch did not touch
   skipped. A notice saying the range cannot be read is not a no: read the range yourself.
4. **The bar is BOUNDED** by the `gate-backstop` fact `--preflight` pinned from `GATE_PROFILE_CMD`,
   or `GATE_BOUND` without a profile. A bar killed after it acquired the repository leaves
   `gates-green` unmet saying it never RETURNED, which is not a FAILED leg.
5. **The close BLOCKS on any unmet Definition-of-Done item.** Two are yours to attest: the reap,
   which `--landed` READS BACK against the listing the stop-guard records, so attest it honestly, and
   the parked decisions, which have no observer and are not a machine verdict. On
   `authorization-reachable` or `pieces-complete` the answer is never an override: `--abort` is the
   honest exit, and the refusal names the rule and the exit. **Write each attestation with the
   verb**, never by editing the record: `--attest <slug> --item keepalive-reaped` once
   `KEEPALIVE_DELETE` reaped the idle-wake, and `--item parked-decisions-surfaced`, optionally
   `--value "yes, <n> surfaced"`, a count `--close` checks against the record's surfaced lines,
   `history` rows and this close's own overrides excluded.
6. **A bar exiting 3, TREE MOVED, is re-run once by the item**; a second is unmet and yours to find.
7. **An INHERITED red is not yours to override.** Under `land`, the kit default, an inherited-only
   red is met at any age, and a leg older than the age bound has its ask filed BLOCKER; under a
   declared `park` the item prints the inherited-red hold, and the Skill's hold routing applies.
   `--override gates-green` and `--abort --code gate-red-out-of-scope` are refused unless every red
   leg reads INHERITED at HEAD. You may instead ABSORB the red on
   `UNATTENDED-STOPS.md` §13's four conditions, in a commit of its own.
8. **An override names its item and a reason, one pair per unmet item**:
   `--close <slug> --override <item> --reason "<why>"`, repeated. A `--override` without its own
   `--reason` is refused before anything is written; the override surfaces in the wrap-up as a
   parked entry.
9. **A unit you cannot finish is carried forward, not overridden.** At the close a park is never an
   abort: take the exit `UNATTENDED-STOPS.md` §15's close-decision table names, for a partial build
   the carry-forward term. A unit of the roster the run started with, waiting on an open ask this
   build filed, gets spec status `DEFERRED` with `closes` or `advances` naming that ask, and
   `--rescope <slug> --act defer --item <unit-id> --reason "<why it waits>"`. `build-complete` then
   meets and prints one `carried forward` line per unit. It stays unmet, naming the unit and the
   condition, when the unit was added during the run, its ask is not open, or a CLOSED unit declares
   `consumes-from` onto it; that build is a `--handoff` under `owner-decision`, never an override.

### Record the run

Binds only where the tool root holds the runlog kit; test for it first, and where absent skip
every step and say so in the wrap-up. `runlog.py record <slug> --write` writes ONE closed-schema
record into the build folder and prints its two follow-ups: re-render the build index, and commit
under a subject naming the slug and no unit id. A run that served no spec-defined unit gets the
no-record line, which is the answer. Three placements, each riding the commit that carries the
run-state file the verb just staged: **after `--abort`**, which renders, re-indexes and stages it
itself; **after `--close` on every run that lands**, riding the close's records commit under
`primary` and committed by the verb under `in-place`; and **under `primary`, after `--landed`**, in
the LANDED record commit, yours, re-rendering the SAME file. **Never between the lander's push and
`--landed`**: a commit there moves HEAD off the lander marker and `--landed` refuses at check 34. A
render that refuses blocks nothing; say so in the wrap-up.

### Land

Under `primary`, run `LANDER` from the primary tree; under `in-place`, `LANDER --land --slug <slug>`
from this worktree, then `--landed`, which there OBSERVES and writes nothing — commit nothing after
the push. Never with a hook-bypass flag: the lander reconciles the remote BEFORE the gate, and the
gate greps the run-state file for the flag. Reconcile from the remote's own default branch onto the
run branch: on a `--prepare` conflict, `git merge <remote>/<default-branch>`, resolve, commit and
prepare again. After ANY merge of the remote's default branch into the run branch, mid-build
included, run `--authorization <slug>` before the next pass and before `--prepare` again: the merge
can bring in a check the README pinned at BASE cannot satisfy, and nothing else reads that item until
the close, after its bar. When the lander cannot COMPLETE the landing — remote unreachable, race retries
exhausted, a close refused because the lander could not observe — push the branch, then `--hold
<slug> --code platform-unavailable --until "after <now + 30 minutes>" --reason "<the lander's last
line>" --reaped <keepalive id>`, the same hold when the branch push ALSO fails because the remote
answers nothing. A RED bar at the push is this run's own: fix it and prepare again; it holds under
that code only when the red is the declared bound firing.

### Mark it landed

Run `--landed <slug>` AFTER the lander returns (`UNATTENDED-STOPS.md` §12; its verb entry above). It
takes the remote's tip whenever your work is on it, and otherwise falls back to the LOCAL default
branch, asserting your BRANCH TIP is its ancestor; read `unpushed-at-landing` before you believe
`landed-anchor`. Under `in-place` it only observes. **Under `primary` run it from the run worktree,
after the lander, with NO commit between the push and this verb**: where a lander marker is declared
it reads CONTAINMENT, so the `--no-ff` merge stamps from your own branch and a marker left by an
earlier landing does not. Then commit the record it writes
and land that commit too — that commit is where the run record re-renders. `--close` alone moves a
run into `LANDING`. On a reap refusal: reap the job, end the turn so the stop-guard records the
listing again, and re-run; a newest line from before the close means end the turn ONCE. A session the
record does not name is refused first and told to `--resume <slug> --keepalive-id <id>`. No stop
ever recorded for the leased session means the hook is unwired, which `adopt-unattended.sh --check`
reports.

### Hold — it cannot continue YET

Use `--hold`, not `--abort`, when what stopped the run is not the run's to fix and not permanent: a
usage limit, an overloaded API, a degraded host, an owner action, a red you inherited and may not
absorb. Commit everything and push the branch first; reap the keepalive and name it with
`--reaped <id>`, or `--keepalive-unreachable <node>` from another node. Codes and conditions are
`UNATTENDED-STOPS.md`'s. A hold on a review that deferred twice adds `--pending-run <runId>`, and the
take-over prints the relaunch to run before anything else. **Then file the restart it printed**: on
`none`, file nothing and stop; otherwise, in order, (1) `RESUME_SCHEDULE_DELETE` against the printed
NAME, going on when no task has it, then (2) `RESUME_SCHEDULE_CREATE` under that name, at that exact
instant, ONE-SHOT, with the three printed prompt lines copied VERBATIM, neither rewritten nor given
the hold reason. The carrier must be DURABLE; the keepalive's scheduler is session-scoped, and the
kit gate reds a conf that names it here.

### Hand it off — done, but you may not land it

`--handoff <slug> --code owner-landing|owner-decision --reason "<why an owner has to take it from
here>" --reaped <the keepalive id you just deleted>`. Use it, not `--abort`, when the work is sound
and the one step left is the owner's: the landing itself, from a node that may not land or onto an
order only the owner sets, or a decision the mandate does not delegate. `ABORTED` means DISCARD, and
a run whose work then lands anyway leaves a record that contradicts git for good. `owner-landing`
means nothing to decide, and is refused unless the last bar the record names reads GREEN on this
tree or every red leg reads INHERITED: an OWN red is yours to fix, or to hand off as a decision.
`owner-decision` means one parked decision stands first: `--park` it before you hand off. It is a
hold with the condition fixed at `owner`, so everything `--hold` asks applies — commit, push the
branch, reap and name the keepalive — but no durable restart is owed and nothing is filed. It
writes the landing recipe as a `handoff` row and prints it; that line is what the owner runs, so
put nothing in the reason it already says. Commit the staged record, push the branch, then stop.

The recipe ends with `--settle <slug>`, and you run it yourself when you find a landed hand-off
still recorded HELD: every reader already reads it `LANDED (attended)`, and this writes it. It
stages and never commits, so the settle commit rides the next landing from that tree; the same verb
records where an older `ABORTED` run's work landed, marks a run whose lease died after its work
landed `abandoned`, and refuses anything git does not prove.

### Abort — it cannot finish

`--abort <slug> --code <halt-code> --reason "<what stopped it, and what you refused to decide>"`.
Both are required: the reason is prose for the owner, the code is what the status line, the resume
path and the gate leg join on. No catch-all member exists: take the closest code, put the specifics
in the reason, and say so. Both attestations come first. An abort neither merges nor pushes, and the
verb stages the run record beside the ABORTED record, so commit them together.

### Reap

Delete the idle-wake with `KEEPALIVE_DELETE` before you finish, and attest `keepalive-reaped`.
Nothing else can: an unreaped job is orphaned in a store no later run can see.
