<!-- gov:kit unattended@1.29 -->
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
  turn that was not needed.
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
- `--status` — one line: the phase, the first non-terminal unit, and the parked counts, then the
  fields that print only when there is something to report — the resume tick's attempts, and
  `keepalive <id> present|absent in the harness listing at <utc>` from the stop-guard's newest
  sidecar line, whatever its phase, omitted when the record names no keepalive id or no line
  exists. The line stays ONE line: a field joins it or does not print, and the suite arms that.
- `--audit` — one line per unit whose dispatch rows at their newest anchor, taken together, are still
  open and whose spec is not terminal: how long the TREE has been idle (newest write, newest commit) and `PROGRESSING` or `STALLED` against `UNIT_STALL_BOUND`, a
  `STALLED` line followed by one remedy line. Read-only; the idle-wake runs it. It cannot see what
  the unit is doing or whether a process is stuck — its figures are properties of the tree.
- `--liveness` — key: value lines and one verdict for an OUT-OF-SESSION reader: the phase, the
  lease, whether the recorded pid exists AND is the leased process (image and start time, not the
  number alone), seconds since anything moved, the last recorded stall, `TERMINAL`,
  `FINISHED-UNSTAMPED`, `UNBOUND`, `STALE` or `LIVE`, and last the `stale-bound` the verdict was
  graded against, so the tick bounds its own reads by this reader's number. Read-only; the
  stop-guard, the stall-recorder's readers and the resume tick call it rather than deciding for
  themselves. It cannot see what the session is doing or whether a process is hung — existence is
  not progress.
- `--resume` — re-enters the run from the run-state file; must agree with `--status`. With
  `--keepalive-id <id>` it REPLACES the lease — keepalive, session, pid — so a resumed session's
  record names the session that now holds it; refused on a terminal record.
  `--scheduled <held-at>` marks it as the restart a DURABLE schedule issued, and is the only
  restart one may issue. It refuses, numbered and before any write, unless the record is HELD, its
  `held-at` equals the value passed, and — under `ANCHOR_SCOPE=published` — the tip the remote
  advertises for the run branch is HEAD or an ancestor of it; an unreachable remote refuses too.
  On success the take-over runs unchanged and still requires the session's own `--keepalive-id`,
  and its history row carries `scheduled` rather than `manual`. `UNATTENDED-STOPS.md` is the
  contract; the rules are not restated here.
- `--close` — evaluates the DoD set, blocks on any unmet item, records any override. The only writer
  of `LANDING`, and it runs BEFORE the landing it authorises, so it cannot observe one.
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
  the id was ever this run's job.
- `--rescope` — records an AMENDMENT to the build's own scope: `--act retire|supersede|add`, the unit
  as `--item`, an optional `--successor`, and a reason. M3 delegates that scope and M2 names the three
  acts; this verb is the record. It RECORDS rather than acts: a row derived from the change it just
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
  one thing here that is unchanged; a unit's own rows are never siblings of each other. Before any of that it runs the DECLARED spec-token checker, `SPEC_TOKENS_CLI`, over the
  live tree and refuses the dispatch when it exits non-zero: the checker's bar join grades LIVE specs,
  an unattended build closes each unit spec in its own build commit, and this verb is the one point
  that sees a spec before its unit builds. A blank or absent key is an ANNOUNCED skip on stdout,
  never a silent pass.
- `--review` — records ONE review round for a subject and reports what the loop is doing:
  `CONVERGING`, `CONVERGED`, `NON-CONVERGENT`, `CEILING` or `BOUNDED`. The round is an append-only
  `review` line in the parked region, a `history` kind, so it never inflates the count of decisions
  the owner must be shown. A round re-arms the loop only if its confirmed-blocker count is STRICTLY
  smaller than the round before — and a subject that is NOT the build slug, a spec audit, takes at
  most the declared `REVIEW_ROUNDS` rounds (kit default 1) before it exits `BOUNDED`; the build slug
  is the closing diff review and its bound is the runaway ceiling, so it converges or backstops as it
  always did. At a TERMINAL exit — `NON-CONVERGENT`, `CEILING` or `BOUNDED` — the round RECORDS its
  disposition, and `promote` is the ONLY value a terminal exit can record: every such exit carries at
  least one BLOCKER by construction, since a zero count is `CONVERGED`, and the severity rule the
  Skill's exit bullet states promotes every blocker, so `--disposition promote` is REQUIRED there and
  `fold` beside a standing blocker is REFUSED rather than written. `fold` survives as the reading of
  a record that exited with nothing above MEDIUM, which the driver reaches only at `CONVERGED` with
  no high, and that row needs no field. On `CONVERGED` an optional `--disposition promote` is
  ACCEPTED, never required, for the round whose highs stood: it is the value that demands new unit
  ids, and a mixed exit takes the value that demands something, so the gate counts the unit a high
  became instead of reading the promotion as nothing. A record naming no value where one is owed
  leaves the gate inferring one from ids. It refuses a verdict or a disposition outside its closed
  set, a missing subject or count, a terminal exit carrying no disposition, `fold` at a terminal
  exit, a disposition on a `CONVERGING` round, and a round on a subject whose loop has already ended.
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
  a code or condition outside its grammar, and a keepalive neither reaped nor recorded unreachable,
  because a job still firing into a held run re-dispatches its units at the next tick. One
  exception to the published-tip clause: under `--code platform-unavailable`, and only when the
  remote does not ANSWER, it accepts the unpublished tip and records it as `hold-unpushed`. In the
  SAME write it decides whether a DURABLE restart is owed and records `resume-owed` and
  `hold-streak`, printing the schedule name, its fire instant and the prompt for the agent to file.
  An optional `--pending-run <runId>` names the Workflow run of a review that deferred twice; it is
  recorded as `hold-run`, rewritten EMPTY by a hold without it, printed on the HELD checkpoint and
  named by a take-over's relaunch line, and a value outside 1 to 64 letters, digits, `_` and `-` is
  refused with the rest. The contract is `UNATTENDED-STOPS.md`.
- `--abort` — the sole producer of `ABORTED`. It requires a recorded reason, a HALT CODE from the
  effective vocabulary, and both agent-attested items, and no machine item: an aborted run landed
  nothing, so the machine items assert obligations it does not have, while the idle-wake is still
  orphaned and the parked decisions still unseen. The code is validated before it is recorded and the
  refusal names the legal set; it is the twelfth authored fact, and it exists because one terminal
  phase said a run stopped and never said why.
